from django.db import models
from django.urls import reverse
from users_auth.models import CustomUser


class Complain(models.Model):
    title = models.CharField(max_length=200)
    AREA_CHOICES = (
        ('H', 'hostel'),
        ('A', 'academics'),
        ('C', 'colony'),
    )
    area = models.CharField(
        max_length=1,
        choices=AREA_CHOICES,
        default='H'
         )

    TAGS_CHOICES = (
        ('G', 'green campus'),
        ('E', 'electrical'),
        ('C', 'civil'),
    )
    tags = models.CharField(
        max_length=1,
        choices=TAGS_CHOICES,
        default='G'
         )

    TYPE_CHOICES = (
        ('I', 'individual'),
        ('G', 'general'),
        
    )
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='G'
         )
    details = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    avail = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)
    by = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='profile')
    priority = models.IntegerField(default=0)
    
    NEED_CHOICES = (
        ('R', 'repair'),
        ('C', 'change'),
    )
    need = models.CharField(
        max_length=1,
        choices=NEED_CHOICES,
        default='R'
         )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comportal:detail', kwargs={'pk': self.pk})

class Post(models.Model):
    complain = models.ForeignKey(Complain, on_delete = models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    by = models.CharField(max_length=50)

    def __str__(self):
        return self.text
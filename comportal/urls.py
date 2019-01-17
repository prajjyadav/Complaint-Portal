from django.urls import path
from .models import Complain
from django.views.generic import ListView

from . import views

app_name = 'comportal'

urlpatterns = [
    # path('', ListView.as_view(
    #     queryset=Complain.objects.all().order_by('-pub_date')),
    #      name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('section/', views.AdminView.as_view(), name='admin-sec'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.detailViewNew, name='detail'),
    path('<int:pk>/prioritize', views.prioritize, name='prioritize'),
    path('<int:pk>/pdf', views.pdf, name='complain-pdf'),
    path('<int:pk>/statusupdate', views.statusupdate, name='status-update'),
    path('add/', views.CreateComplain.as_view(), name='newcomplain'),
    path('lodged/', views.LodgedComplain.as_view(), name='lodged-complains'),
    path('<int:pk>/process', views.process, name='process'),
    path('<int:pk>/done', views.done, name='done'),
    path('update/<int:pk>/', views.UpdateComplain.as_view(), name='update-complain'),
    path('delete/<int:pk>/', views.DeleteComplain.as_view(), name='delete-complain'),
    path('user/<str:username>', views.UserComplains.as_view(), name='user-complains'),
    path('hostel/', ListView.as_view(
        queryset=Complain.objects.filter(area='H').order_by('-pub_date')),
         name='index-hostel'),
    path('academics/', ListView.as_view(
        queryset=Complain.objects.filter(area='A').order_by('-pub_date')),
         name='index-academics'),
    path('colony/', ListView.as_view(
        queryset=Complain.objects.filter(area='C').order_by('-pub_date')),
         name='index-colony'),
    path('green/', ListView.as_view(
        queryset=Complain.objects.filter(tags='G').order_by('-pub_date')),
         name='index-green'),
    path('electrical/', ListView.as_view(
        queryset=Complain.objects.filter(tags='E').order_by('-pub_date')),
         name='index-electrical'),
    path('civil/', ListView.as_view(
        queryset=Complain.objects.filter(tags='C').order_by('-pub_date')),
         name='index-civil'),
    path('recents/', ListView.as_view(
        queryset=Complain.objects.all().order_by('-pub_date')[:5]),
         name='index-recents'),
    path('last/', ListView.as_view(
        queryset=Complain.objects.all().order_by('pub_date')[:5]),
         name='index-last'),
    path('unprocessed/', ListView.as_view(
        queryset=Complain.objects.filter(status=0).order_by('-pub_date')),
         name='index-unprocessed'),
    path('processing/', ListView.as_view(
        queryset=Complain.objects.filter(status=1).order_by('-pub_date')),
         name='index-processing'),
    path('resolved/', ListView.as_view(
        queryset=Complain.objects.filter(status=2).order_by('-pub_date')),
         name='index-resolved'),
    path('priority/', ListView.as_view(
        queryset=Complain.objects.all().order_by('priority')),
         name='index-priority'),
    
]

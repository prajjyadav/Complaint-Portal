from .models import Post
from django import forms

# class UserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     islove = forms.CharField()
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password','islove']
    
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text',]
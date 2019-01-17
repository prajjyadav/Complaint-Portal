from django.urls import path
from comportal.models import Complain
from django.views.generic import ListView

from . import views
from comportal import views as comp_views

app_name = 'users_auth'

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('profile/', views.profile, name='user-profile'),
    path('<int:pk>/update/', views.UserUpdateFormView.as_view(), name='update-profile'),
    path('<int:pk>/clear/', views.clear, name='clear-noti'),
]
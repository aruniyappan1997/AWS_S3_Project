from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_profile, name='upload_profile'),
    path('', views.user_list, name='user_list'),
]

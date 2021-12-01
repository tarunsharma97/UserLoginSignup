from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.signIn),
    path('home/', views.home, name='home'),
    path('postsignIn/', views.postsignIn),
    path('resetpass/', views.resetpass,),
    path('postresetpass/', views.postresetpass),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
]
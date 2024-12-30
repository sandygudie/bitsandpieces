from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    #  path('<str:slug>', views.post, name='post'),
     path('post/<str:slug>/', views.post, name='post'),
]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('index/', views.index, name='index-index'),
    path('about/', views.about, name='blog-index'),
]
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name='index-index'),
    path('about/', views.about, name='blog-index'),
]
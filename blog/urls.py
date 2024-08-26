from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),
    path('post_detail/<int:pk>', views.post_detail, name='blog-post-detail'),
]
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:id>/', views.posts_detail, name='posts_detail'),
]

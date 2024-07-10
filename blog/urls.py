from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts_list'),
    # path('posts/', views.PostListView.as_view, name='posts_list'),
    path('posts/<int:pk>/', views.posts_detail, name='posts_detail'),
    # path('posts/<int:pk>/', views.PostDetailView.as_view, name='posts_detail'),
    path('posts/<post_id>/comment', views.post_comment, name='post_comment'),
    path('ticket', views.ticket, name='ticket'),
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts_list'),
    # path('posts/', views.PostListView.as_view, name='posts_list'),
    path('posts/<int:pk>/', views.posts_detail, name='posts_detail'),
    # path('posts/<int:pk>/', views.PostDetailView.as_view, name='posts_detail'),
    path('posts/<post_id>/comment', views.post_comment, name='post_comment'),
    path('ticket', views.ticket, name='ticket'),
    path('profile/create_post/', views.create_post, name='create_post'),
    path('search', views.post_search, name='post_search'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete_post/<post_id>', views.delete_post, name='delete_post'),
    path('profile/edit_post/<post_id>', views.edit_post, name='edit_post'),
    path('profile/delete_image/<image_id>', views.delete_image, name='delete_image'),
    # path('login', views.user_login, name='login'),
    # path('logout', views.log_out, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

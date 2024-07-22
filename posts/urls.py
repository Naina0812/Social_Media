from django.urls import path
from . import views
from .views import  PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, LikeView, AllLikeView


urlpatterns = [
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/like/', LikeView, name='post-like'),
    path('liked-posts/', AllLikeView, name='all-like'),
]
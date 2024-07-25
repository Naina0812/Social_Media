from django.urls import path
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    UserCommentListView,
    AllLikedCommentsView
)

urlpatterns = [
    path('comment/user/<str:username>/', UserCommentListView.as_view(), name='user-comments'),
    path('comment/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('liked-comments/', AllLikedCommentsView.as_view(), name='all-liked-comments'),
]

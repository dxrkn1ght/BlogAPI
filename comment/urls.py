from django.urls import path
from .views import CommentListCreateAPIView, CommentDetailAPIView, NestedCommentAPIView


app_name = 'comments'


urlpatterns = [
    path('', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('<int:comment_id>/replies/', NestedCommentAPIView.as_view(), name='nested-comments'),
]
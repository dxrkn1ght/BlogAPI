from django.urls import path
from .views import TagListCreateAPIView, TagPostsAPIView

urlpatterns = [
    path('api/tags/', TagListCreateAPIView.as_view()),
    path('api/tags/<int:tag_id>/posts/', TagPostsAPIView.as_view()),
]
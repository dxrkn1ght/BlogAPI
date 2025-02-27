from django.urls import path
from .views import TagListCreateAPIView, TagPostsAPIView

urlpatterns = [
    path('', TagListCreateAPIView.as_view()),
    path('<int:tag_id>/posts/', TagPostsAPIView.as_view()),
]
from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView, CategoryPostsAPIView


urlpatterns = [
    path('', CategoryAPIView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('<int:category_id>/posts/', CategoryPostsAPIView.as_view(), name='category-posts'),
]
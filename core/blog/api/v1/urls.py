from django.contrib import admin
from django.urls import path, include
from .views import (PostViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

app_name = 'api-v1'

urlpatterns = [
    path('', include(router.urls)),
]
# urlpatterns = [
    # path('posts/', blogPostList, name='post_list'),
    # path('posts/', BlogPostList.as_view(), name='post_list'),
    # path('posts/<int:pk>/', BlogPostDetail.as_view(), name='post_detail'),
    # path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_list'),
# ]

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # Frontend views (public)
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # API v1
    path('api/v1/', include('blog.api.v1.urls')),
]

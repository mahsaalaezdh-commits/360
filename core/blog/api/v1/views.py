from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import RedirectView, TemplateView
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.generics import (GenericAPIView, 
                                    ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,
                                    UpdateAPIView, DestroyAPIView, ListCreateAPIView)

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets

from .serializers import BlogPostSerializers
from blog.models import BlogPost, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]





'''
class BlogPostList(GenericAPIView, ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializers
    queryset = BlogPost.objects.all()

class BlogPostDetail(GenericAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializers
    queryset = BlogPost.objects.filter(status='published')

'''











'''
class BlogPostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializers

    def get(self, request):
        posts = get_object_or_404(BlogPost).objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializers

    def get_object(self, pk):
        return get_object_or_404(BlogPost, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''










'''
@api_view(['GET'])
def blogPostList(request):
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializers(posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def blogPostDetail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'GET':
        serializer = BlogPostSerializers(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BlogPostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def blogPostCreate(request):
    if request.method == 'POST':
        serializer = BlogPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
'''
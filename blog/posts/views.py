from rest_framework import mixins, generics
from .models import Post
from .serializers import *
from rest_framework.permissions import (IsAdminUser, 
                                        IsAuthenticated, 
                                        IsAuthenticatedOrReadOnly, 
                                        BasePermission, SAFE_METHODS)

from rest_framework.pagination import PageNumberPagination


class IsAuthenticatedOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.user == request.user


class PagePagination(PageNumberPagination):
    page_size=1


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = PagePagination


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAdminUser,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset  = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
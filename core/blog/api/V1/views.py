from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework.response import Response
from .serializers import PostSerialilzer, CategorySerializer
from ...models import Post, category
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets
from .permission import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefultPagination


"""
from rest_framework.decorators import api_view,permission_classes

@api_view(["GET","POST"]) 
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET" :
        posts=Post.objects.filter(status=True)
        serializer=PostSerialilzer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer=PostSerialilzer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def postDetail(request,id):
    post=get_object_or_404(Post,pk=id)
    if request.method== 'GET':
        serializer=PostSerialilzer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer=PostSerialilzer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item removed successfully"})        
        """


'''
"""create and list of post"""
class PostList(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerialilzer
    def get(self,request):
        """retrieving a list of posts"""
        posts=Post.objects.filter(status=True)
        serializer=PostSerialilzer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """create post with provided data"""
        serializer=PostSerialilzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        
class PostDetail(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=PostSerialilzer

    def get(self,request,id):
        """retrieving the post data"""
        post=get_object_or_404(Post,pk=id)
        serializer=self.serializer_class(post)
        return Response(serializer.data)

    def put(self,request,id):
        """editing the post data"""
        post=get_object_or_404(Post,pk=id)
        serializer=PostSerialilzer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,id):
        """deleting the post object"""
        post=get_object_or_404(Post,pk=id)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
'''


class PostList(ListCreateAPIView):
    """geting list of post and create list"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerialilzer
    queryset = Post.objects.filter(status=True)


"""getting detail of the post and edit plus removing it"""
""""""


class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of the post and edit plus removing it"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerialilzer
    queryset = Post.objects.filter(status=True)


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerialilzer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = category.objects.all()

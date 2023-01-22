from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerialilzer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status
 

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
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
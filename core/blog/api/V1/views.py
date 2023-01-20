from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerialilzer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
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

@api_view()
def postDetail(request,id):
    post=get_object_or_404(Post,pk=id)
    serializer=PostSerialilzer(post)
    return Response(serializer.data)
 
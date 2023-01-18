from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerialilzer
from ...models import Post


@api_view()
def postList(request):
    return Response("ok")

@api_view()
def postDetail(request,id):
    post=Post.objects.get(pk=id)
    serializer=PostSerialilzer(post)
    return Response(serializer.data)

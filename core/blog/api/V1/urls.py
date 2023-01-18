from django.urls import path,include
from . import views

app_name = "api_v1"

urlpatterns=[
    path('post/',views.postList,name='post-list'),
    path('post/<int:id>/',views.postDetail,name="post-detail"),
    ]
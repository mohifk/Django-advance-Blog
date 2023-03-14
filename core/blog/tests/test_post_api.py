import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User

@pytest.fixture
def api_client():
    client=APIClient()
    return client
@pytest.fixture
def common_user():
    user=User.objects.create_user(email="t2@admin.com",password="123")
    return user




@pytest.mark.django_db
class TestPostApi:
    #client=APIClient()
    def test_get_post_response_200_status(self,api_client,common_user):
        user=common_user
        api_client.force_authenticate(user=user)
        url =reverse("blog:api_v1:post-list")
        response= api_client.get(url)
        assert response.status_code==200
    
    def test_create_post_respnse_403_status(self,api_client):
        url=reverse("blog:api_v1:post-list")
        data={"title":"test",
              "content":"description",
              "status":True,
              "published_date":datetime.now() }
     
        response= api_client.post(url,data)
        assert response.status_code==403
    
    def test_create_post_response_201_status(self,api_client,common_user):
        url=reverse("blog:api_v1:post-list")
        data={"title":"test",
              "content":"description",
              "status":True,
              "published_date":datetime.now() }
        user=common_user
        api_client.force_authenticate(user=user)
        response=api_client.post(url,data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self,api_client,common_user):
        url=reverse("blog:api_v1:post-list")
        data={"title":"test",
              "content":"description",
         }
        user=common_user
        api_client.force_authenticate(user=user)
        response=api_client.post(url,data)
        assert response.status_code == 400



 
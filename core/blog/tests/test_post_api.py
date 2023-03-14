import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime

@pytest.mark.django_db
class TestPostApi:
    client=APIClient()
    def test_get_post_response_200_status(self):
        url=reverse("blog:api_v1:post-list")
        response= self.client.get(url)
        assert response.status_code==200

    def test_create_post_respnse_401_status(self):
        url=reverse("blog:api_v1:post-list")
        data={"title":"test",
              "content":"description",
              "status":True,
              "published_date":datetime.now() }
        response=self.client.post(url,data)
        assert response.status_code==407
from django.test import SimpleTestCase,TestCase
from datetime import datetime
from ..models import Post,category
from django.contrib.auth import get_user_model
from accounts.models import User,Profile
from ..models import category

class TestPostModel(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(email="te@test.com",password='A@123456')
        self.profile=Profile.objects.create(
            user=self.user,
            first_name='test_fname',
            last_name='tlast_name',
            description='TESTED'
            )
    def test_create_post_form_with_valid_data(self):
        # user=User.objects.create_user(email="te@test.com",password='A@123456')
        # profile=Profile.objects.create(user=user,first_name='test_fname',last_name='tlast_name',description='TESTED')
        post=Post.objects.create(
            author=self.profile,
            title='test',
            content='describtion',
            status=True,
            category=None,
            published_date=datetime.now()
            )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())        
        self.assertEquals(post.title,'test')
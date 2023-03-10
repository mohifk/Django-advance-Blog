from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from ..views import IndexView,PostListView,PostDetailView

class TestUrl(SimpleTestCase):
    def test_blog_index_urls_resolve(self):
        url=reverse('blog:index')
        self.assertEquals(resolve(url).func.view_class,IndexView)
    def test_blog_post_list_urls_resolve(self):
        url=reverse('blog:post_list')
        self.assertEquals(resolve(url).func.view_class,PostListView)
    def test_blog_post_detail_urls_resolve(self):
        url=reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class,PostDetailView)
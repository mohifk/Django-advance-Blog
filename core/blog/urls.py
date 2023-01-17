from . import views
from django.urls import path,include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
app_name="blog"
urlpatterns = [
    #path('fbv-index',views.indexView,name='fbv-index'),
    #path('cbv-index',TemplateView.as_view(template_name='index.html',extra_context={'name':'mohi'})),
    #path('cbv-index',views.IndexView.as_view(),name='cbv-index'),
    #path('goto_googl',RedirectView.as_view(url='https://digikala.com/'),name='google'),
    #path('go_to_index',RedirectView.as_view(pattern_name="blog:cbv-index"),name='redirect_to_index'),
    #path('go-to-maktab/<int:pk>/',views.Redirecttomaktab.as_view(),name='redirect-to-maktab'),
    path('post/',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="post-detail"),
    path('post/create/',views.PostCreateView.as_view(),name="post-create"),
    path('post/<int:pk>/edit/',views.PostEditView.as_view(),name="post-edit"),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name="post-delete"),
    path('api/v1/',include('blog.api.V1.urls'))
    ]
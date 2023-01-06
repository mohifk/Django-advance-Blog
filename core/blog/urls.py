from . import views
from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('fbv-index',views.indexView,name='fbv-index'),
    #path('cbv-index',TemplateView.as_view(template_name='index.html',extra_context={'name':'mohi'})),
    path('cbv-index',views.IndexView.as_view(),name='cbv-index')
    ]
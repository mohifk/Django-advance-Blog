from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import redirect,get_object_or_404
from .models import Post
from django.views.generic import ListView , DetailView ,FormView
from.forms import PostForm
def indexView(request):

    '''a function based view to show index page'''
'''
    name='ali'
    context={'name':name}
    return render(request,"index.html",context)'''

class IndexView(TemplateView):
    '''a class based view to show index page'''

    template_name ='index.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["name"]="mohi"
        context["posts"]=Post.objects.all()
        return context  
'''FBV for redirect 
def redirecttomaktab(request):
    return redirect('https://digikala.com')
'''
class Redirecttomaktab(RedirectView):
    url = 'https://digikala.com'

    def get_redirect_url(self, *args, **kwargs):
        post=get_object_or_404(Post,pk=kwargs['pk'])
        print('post')
        return super().get_redirect_url(*args, **kwargs)

class PostListView(ListView):
   model=Post
   #queryset=Post.objects.all()
   context_object_name="posts"
   paginate_by=3
   ordering='-id'

#    def get_queryset(self):
#         posts=Post.objects.filter(status=True)
#         return posts
class PostDetailView(DetailView):
    model= Post

class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
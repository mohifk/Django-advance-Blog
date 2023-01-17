from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.shortcuts import redirect,get_object_or_404
from .models import Post
from django.views.generic import ListView , DetailView ,FormView,CreateView,UpdateView,DeleteView
from.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin




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

class PostListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
   permission_required = 'blog.view_post'
   #model=Post
   queryset=Post.objects.all()
   context_object_name="posts"
   #paginate_by=3
   ordering='-id'

#    def get_queryset(self):
#         posts=Post.objects.filter(status=True)
#         return posts
class PostDetailView(DetailView):
    model= Post

'''class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)'''

class PostCreateView(CreateView):
    model=Post
    #fields = ['author','title','content','status','category','published_date']
    success_url='/blog/post/'
    form_class=PostForm
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostEditView(UpdateView):
    model=Post
    form_class=PostForm
    success_url='/blog/post/'

class PostDeleteView(DeleteView):
    model=Post
    success_url='/blog/post/'
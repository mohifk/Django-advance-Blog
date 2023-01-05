from django.shortcuts import render
def indexView(request):
    name='ali'
    context={'name':name}
    return render(request,"index.html",context)
# Create your views here.

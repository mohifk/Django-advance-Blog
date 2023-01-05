from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Post(models.Model):
    ''' this is a class to define posts for blog '''
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True)
    title= models.CharField(max_length=250)
    content=models.TextField()
    status = models.BooleanField()
    category=models.ForeignKey('category',on_delete=models.SET_NULL,null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField()

    def __str__(self) :
        return self.title

class category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
# Create your models here.

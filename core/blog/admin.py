from django.contrib import admin
from .models import Post,category
class PostAdmin(admin.ModelAdmin):
    list_display=["author","title","status","category","create_date","published_date"]

admin.site.register(category)
admin.site.register(Post)
# Register your models here.

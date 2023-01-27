from rest_framework import serializers
from ...models import Post,category

# class PostSerialilzer(serializers.Serializer):
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)

class PostSerialilzer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','title','author','content','category','status','created_date','published_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['id','name']
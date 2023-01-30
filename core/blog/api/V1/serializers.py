from rest_framework import serializers
from ...models import Post,category

# class PostSerialilzer(serializers.Serializer):
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)

class PostSerialilzer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    
    class Meta:
        model=Post
        fields=['id','title','author','content','snippet','category','status','relative_url','created_date','published_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['id','name']
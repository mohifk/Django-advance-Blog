from rest_framework import serializers
from ...models import Post,category

# class PostSerialilzer(serializers.Serializer):
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)

class PostSerialilzer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')

    class Meta:
        model=Post
        fields=['id','title','author','content','snippet','category','status','relative_url','absolute_url','created_date','published_date']
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['id','name']
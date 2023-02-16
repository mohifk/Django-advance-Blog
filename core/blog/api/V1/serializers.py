from rest_framework import serializers
from ...models import Post,category
from accounts.models import Profile

# class PostSerialilzer(serializers.Serializer):
    # id=serializers.IntegerField()
    # title=serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['id','name']   

class PostSerialilzer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    #category=serializers.SlugRelatedField(many=False,slug_field='name',queryset=category.objects.all())
    class Meta:
        model=Post
        fields=['id','title','author','image','content','snippet','category','status','relative_url','absolute_url','created_date','published_date']
        read_only_fields=['author']
    def get_abs_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj)
        
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet')
            rep.pop('relative_url')
            rep.pop('absolute_url')
        rep['category']=CategorySerializer(instance.category,context={'request':request}).data
        
        return rep

    def create(self, validated_data):
        validated_data['author']=Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
    

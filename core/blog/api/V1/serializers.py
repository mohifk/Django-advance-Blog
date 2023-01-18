from rest_framework import serializers

class PostSerialilzer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    
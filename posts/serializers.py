# posts/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'media_url', 'description', 'created', 'updated','likes']
        read_only_fields = ['id', 'user', 'created', 'updated']

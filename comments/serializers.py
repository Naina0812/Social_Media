from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'comment', 'created', 'updated','likes']
        read_only_fields = ['id', 'user', 'created', 'updated','likes']

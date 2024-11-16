from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user', 'comments', 'comment_count']

    def get_comments(self, obj):
        # Get the 3 most recent comments
        comments = obj.comments.select_related('user').order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data

    def get_comment_count(self, obj):
        return obj.comments.count()

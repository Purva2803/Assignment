from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.db.models import Prefetch
from .models import Comment

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.select_related('user').order_by('-timestamp')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['max_comments'] = 3
        return context

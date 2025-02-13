from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    comment = models.TextField()  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'Comment {self.id} by {self.user.username} on Post {self.post.id}'

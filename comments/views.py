from django.shortcuts import render
from .models import Comment

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = Comment.objects.get(pk=pk)
    return render(request, 'comments/comment_detail.html', {'comment': comment})

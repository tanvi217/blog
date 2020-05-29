from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    """ Displays lists """
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

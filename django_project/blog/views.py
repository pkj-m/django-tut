from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based list view 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default template name is <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # default context object name is 'object'
    ordering = ['-date_posted'] # list in newest to oldest of date posted

# detail view of a blog post
class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'Pankaj'})


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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
    paginate_by = 5 # number of posts per page


# class based list view for posts of a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # default template name is <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # default context object name is 'object'
    paginate_by = 5 # number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# detail view of a blog post
class PostDetailView(DetailView):
    model = Post

# create view of a blog post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # before you validate the form, make sure the author is set to user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# update a pre-existing blog 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # before you validate the form, make sure the author is set to user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check if the author is the one making the update, derived from UserPassesTextMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# delete post
# detail view of a blog post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # add a success url to redirect to
    success_url = '/'

    # check if the author is the one making the update, derived from UserPassesTextMixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html', {'title': 'Pankaj'})


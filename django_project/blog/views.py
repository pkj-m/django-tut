from django.shortcuts import render

posts = [
    {
        'author': 'Pankaj',
        'title': 'Blog Post 1',
        'content': 'Content of post 1',
        'date_created': 'January 7, 2021'
    },
    {
        'author': 'harsh',
        'title': 'Blog Post 2',
        'content': 'Content of post 2',
        'date_created': 'January 3, 2021'
    },

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'Pankaj'})
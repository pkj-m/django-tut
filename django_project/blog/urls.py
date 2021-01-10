from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [

    #path('', views.home, name='blog-home'),

    # class views need a .as_view() method at the end 
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about')
]

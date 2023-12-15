from django.shortcuts import render
from .models import Post,Response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

    
class PostList(ListView):
    raise_exception = True   
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
        
    
    
class PostDetail(DetailView):
    raise_exception = True
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
class PostCreate(PermissionRequiredMixin,CreateView):
    raise_exception = True
    permission_required = ('simpleapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
class PostUpdate(PermissionRequiredMixin,UpdateView):
    raise_exception = True
    permission_required = ('simpleapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
class PostDelete(PermissionRequiredMixin,DeleteView):
    raise_exception = True
    permission_required = ('simpleapp.delete_posts',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    
class Response(ListView):
    def 
    



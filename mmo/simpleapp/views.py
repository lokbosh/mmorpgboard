from django.shortcuts import render
from .models import Post,Response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .filters import PostFilter
    
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
    
class ResponseList(ListView):
    raise_exception = True
    model = Response
    ordering = '-dateCreation'
    template_name = 'response.html'
    context_object_name = 'response'
    paginate_by = 10 
    
class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


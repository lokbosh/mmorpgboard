from typing import Any
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,ResponseForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from .filters import PostFilter
from django.contrib import messages
class PostList(ListView):
    raise_exception = True   
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs
        
class PostResponseCreate(CreateView):
    raise_exception = True 
    model = Response
    template_name = 'post.html'
    form_class = ResponseForm
    permission_required = ('simpleapp.view_post',)
    
    
    def form_valid(self, form):
        response = form.save(commit=False)
        response.author_id = self.request.user.pk
        response.post_id = self.kwargs.get('pk')
        response.save()
        return super().form_valid(form)
    
    
class PostDetail(DetailView,PostResponseCreate):
    raise_exception = True
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(post_id=self.object.pk)
        return context
    
        
class PostCreate(CreateView):
    raise_exception = True
    permission_required = ('simpleapp.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
class PostUpdate(UpdateView):
    raise_exception = True
    permission_required = ('simpleapp.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    
class PostDelete(DeleteView):
    raise_exception = True
    permission_required = ('simpleapp.delete_posts',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

@login_required   
def profile(request):
    posts = Post.objects.filter(author=request.user)
    responses = Response.objects.filter(post__in=posts)
    profile_post_id = request.GET.get('post_id')
    category_filter = request.GET.get('category')
    if profile_post_id:
        responses = responses.filter(post_id=profile_post_id)
    if category_filter:
        responses = responses.filter(post__category=category_filter)
    return render(request, 'profile.html', {'user': request.user, 'responses': responses})

@login_required
def accept_request(request, response_id):
    response = get_object_or_404(Response, id=response_id)

    if request.user != response.post.author:
        messages.error(request, 'Недостаточно прав для выполнения этого действия.')
        return redirect('profile')

    if response.status != 'undefined':
        messages.error(request, 'Этот запрос уже обработан.')
        return redirect('profile')

    response.status = 'accepted'
    response.save()

    subject = f'Ваш запрос принят'
    message = f'Ваш запрос на объявление "{response.post.title}" был принят.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [response.author.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    messages.success(request, 'Запрос успешно принят.')
    return redirect('profile')

@login_required
def reject_request(request, response_id):
    response = get_object_or_404(Response, id=response_id)

    if request.user != response.post.author:
        messages.error(request, 'Недостаточно прав для выполнения этого действия.')
        return redirect('profile')

    if response.status != 'undefined':
        messages.error(request, 'Этот запрос уже обработан.')
        return redirect('profile')

    response.status = 'rejected'
    response.save()

    subject = f'Ваш запрос отклонен'
    message = f'Ваш запрос на объявление "{response.post.title}" был отклонен.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [response.author.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    messages.success(request, 'Запрос успешно отклонен.')
    return redirect('profile')
    

    
    
    
    

    
    
        
    
        
    



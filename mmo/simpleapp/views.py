from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Response
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,ResponseForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpResponseBadRequest
from .filters import PostFilter
import secrets
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
        
class PostResponseCreate(PermissionRequiredMixin,CreateView):
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

@login_required   
def profile(request):
    posts = Post.objects.filter(author=request.user)
    responses = Response.objects.filter(post__in=posts)
    profile_post_id = request.GET.get('post_id')
    if profile_post_id:
        responses = responses.filter(post_id=profile_post_id)

    return render(request, 'profile.html', {'profile': profile, 'responses': responses})

@login_required
def response_status(request, response_id, action):
    response = get_object_or_404(Response, id=response_id)
    if action == 'accept':
        response.status = 'accepted'
        subject = 'Ваш запрос принят'
    elif action == 'reject':
        response.status = 'rejected'
        subject = 'Ваш запрос отклонен'
    else:
        return HttpResponseBadRequest('Недопустимое действие')

    response.save()
    return redirect('post', post_id=response.post.id)

        
    
@login_required
def request_verification(request):
    # Генерация кода верификации
    verification_code = secrets.token_urlsafe(6)
    
    # Сохранение кода в сеансе Django
    request.session['verification_code'] = verification_code

    # Здесь должна быть логика отправки кода на почту, но мы пропускаем это для примера

    return render(request, 'verification_request.html')

@login_required

def verify_email(request):
    stored_code = request.session.get('verification_code')

    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')

        if entered_code == stored_code:
            request.session['email_verified'] = True
            messages.success(request, 'Ваш аккаунт успешно верифицирован.')
            return redirect('profile')
        else:
            messages.error(request, 'Неверный код верификации.')

    return render(request, 'verify_email.html')
        
    
    
    
    

    
    
        
    
        
    



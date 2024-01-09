from django.urls import path
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,PostResponseCreate,profile,accept_request,reject_request
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',PostList.as_view(),name='posts'),
    path('<int:pk>',PostDetail.as_view(),name='post_detail'),
    path('create/',PostCreate.as_view(),name='post_create'),
    path('<int:pk>/update/',PostUpdate.as_view(),name='post_update'),
    path('<int:pk>/delete/',PostDelete.as_view(),name='post_delete'),
    path('<int:pk>/response/create',PostResponseCreate.as_view(),name='response_create'),
    path('profile',profile,name='profile'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('response/accept/<int:response_id>/', accept_request, name='accept_request'),
    path('response/reject/<int:response_id>/', reject_request, name='reject_request'),
    
]

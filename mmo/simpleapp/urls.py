from django.urls import path
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,PostResponseCreate,profile,verify_email,request_verification
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',PostList.as_view(),name='posts'),
    path('<int:pk>',PostDetail.as_view(),name='post_detail'),
    path('create/',PostCreate.as_view(),name='post_create'),
    path('<int:pk>/update/',PostUpdate.as_view(),name='post_update'),
    path('<int:pk>/delete/',PostDelete.as_view(),name='post_delete'),
    path('<int:pk>/response/create',PostResponseCreate.as_view(),name='response_create'),
    path('profile',profile,name='profile'),
    path('verify_email',verify_email,name='verify_email'),
    path('request_verification',request_verification,name='request_verification'),
    path('logout/',LogoutView.as_view(),name='logout')
]

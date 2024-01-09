from django.urls import path
from .views import SignUp,send_confirmation_code

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    
]
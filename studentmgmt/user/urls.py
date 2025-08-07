from django.urls import path
from .views import security_login

urlpatterns = [
    path('login/', security_login, name='security_login'),
]

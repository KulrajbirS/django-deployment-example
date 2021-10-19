from django.conf.urls import include
from django.urls import path
from learning_permissions import views

app_name = 'learning_permissions'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]

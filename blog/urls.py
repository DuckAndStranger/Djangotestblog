from django.urls import path
from . import views
urlpatterns = [
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='home'),
    path('create', views.add_post, name='create'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name= 'logout')
]
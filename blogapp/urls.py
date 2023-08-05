from django.contrib import admin
from django.urls import path
from blogapp.views import *

urlpatterns = [
    path('index/', index, name="main"),
    path('blog_create/', blog_create, name="create"),
    path('blog_edit/<int:pk>/', edit_blog, name='edit'),
    path('blog_delete/<int:pk>/', delete_blog, name='delete'),
    path('comment_blog/<int:pk>/', comment_blog, name='comment'),
]





from django.contrib import admin
from .models import Post
from django.urls import path

admin.site.register(Post)
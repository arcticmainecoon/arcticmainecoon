from django.contrib import admin
from django.urls import path, include
from .views import home, blog

urlpatterns = [
    path("", home, name="home"),
    path("read/<int:blog_id>/", blog, name="blog")
]

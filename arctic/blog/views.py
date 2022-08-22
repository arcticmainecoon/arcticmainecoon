from django.shortcuts import render
from .models import Blog
from datetime import datetime

def home(request):
    blogs = Blog.objects.all()




    return render(request, "blog/home.html", {
        'blogs': blogs,
    })


# detail
def blog(request, blog_id):

    blog = Blog.objects.get(id=blog_id)

    return render(request, "blog/blog.html", context={
        'blog': blog
    })

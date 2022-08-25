from django.shortcuts import render
from .models import Blog

# Create your views here.
def list_blogs(request):
    blogs = Blog.objects.all()

    return render(request, "blog/home.html", context={
        'blogs': blogs,
    })

def read_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, "blog/blog_detail.html", {
        'blog': blog,
    })
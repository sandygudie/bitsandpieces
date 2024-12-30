from django.shortcuts import render
from .models import Blog


def index(request):
    data = Blog.objects.filter(published=True).values()
    context = {"bloglists": data, }
    # print(context)
    return render(request, "blog/index.html", context)


def post(request, slug):
    data = Blog.objects.get(slug=slug)
    context = {"post": data}
    return render(request, "blog/post.html", context)


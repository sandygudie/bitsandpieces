from django.shortcuts import render, get_object_or_404
from .models import Blog


def index(request):
    data = Blog.objects.filter(published=True).values()
    context = {"bloglists": data, }
    # print(context)
    return render(request, "blog/index.html", context)


def post(request, slug):
    data = Blog.objects.get(slug=slug)
    # data= get_object_or_404(Blog, slug=slug)
    context = {"post": data}
    return render(request, "blog/post.html", context)


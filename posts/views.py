from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, 'index.html')


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, 'posts/list.html', ctx)


def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
            )
            return redirect('posts:list')
    return render(request, 'posts/form.html')


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx ={'post': post}
    return render(request, 'posts/detail.html', ctx)
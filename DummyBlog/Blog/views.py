from django.shortcuts import get_object_or_404, render

from .models import Post


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, 
                            publish__day=day, slug=post, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_list(request):
    posts = Post.published.all()
    return render(request, 'Blog/post/list.html', {'posts': posts})





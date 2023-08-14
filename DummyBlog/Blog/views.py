from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, 
                            publish__day=day, slug=post, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 6) # Создаём пагинатор с разбивкой по 6 постов на страницу
    page_number = request.GET.get('page', 1) # Получаем номер страницы из запроса, 1 - если нет атрибута page
    try:
        posts = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        posts = paginator.page(1)

    return render(request, 'Blog/post/list.html', {'posts': posts})





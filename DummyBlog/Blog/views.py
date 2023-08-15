from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm
from os import environ

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


def post_share(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month, 
                            publish__day=day, slug=post, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = f"{cd['name']} reccomends you read "\
                        f"{post.title}"
            message = cd['comments']
            send_mail(subject, message, environ.get('EMAIL_HOST_USER'), [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'Blog/post/share.html', {'post': post,
                                            'form': form,
                                            'sent': sent})

#class PostListView(ListView):
#    queryset = Post.published.all()
#    context_object_name = 'posts'
#    paginate_by = 3
#    template_name = 'Blog/post/list.html'


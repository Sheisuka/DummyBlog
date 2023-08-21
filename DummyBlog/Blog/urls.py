from django.urls import path
from . import views


app_name = 'Blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/share', views.post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/comment', views.post_comment, name='post_comment')
]

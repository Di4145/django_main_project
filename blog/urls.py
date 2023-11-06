from django.urls import path
from blog.views import blog, detail, like

urlpatterns = [
    path('', blog, name='blog_page'),
    path('detail/<int:article_id>/', detail, name='article_detail'),
    path('like/', like, name='like_set')
]

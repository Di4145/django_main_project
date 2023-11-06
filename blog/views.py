from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from blog.models import Article, Like


# Create your views here.
def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    like_count = article.like_set.count()
    user_id = request.user.id
    if Like.objects.filter(user_id_id=user_id, article_id=article_id).exists():
        button = 'UnLike'
    else:
        button = 'Like'
    return render(request, 'article_detail.html', {'article': article, 'like_count': like_count, 'button': button})


def like(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        article_id = request.POST['article_id']
        if Like.objects.filter(user_id_id=user_id, article_id=article_id).exists():
            new_like = Like.objects.filter(user_id_id=user_id, article_id=article_id)
            new_like.delete()

        else:
            new_like = Like(user_id_id=user_id, article_id=article_id)
            new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

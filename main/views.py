from django.shortcuts import render
from blog.models import Article
# Create your views here.

def main(request):
    articles = Article.objects.all()

    return render(request, 'index.html', {'articles': articles})

def detail(request, article_id ):
    article = Article.objects.get(id=article_id)
    like_count = article.like_set.count()
    return render(request, 'article_detail.html', {'article': article, 'like_count': like_count})
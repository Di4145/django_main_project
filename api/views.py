from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import ArticleSerializers
from blog.models import Article


# Create your views here.


class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()

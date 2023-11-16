from rest_framework import serializers

from blog.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'text', 'created_at', 'update', 'text_1']


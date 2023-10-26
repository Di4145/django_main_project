from django.db import models


# Create your models here.
class Article(models.Model):
    author = models.CharField(max_length=40)
    title = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.CharField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title

    
class Like(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

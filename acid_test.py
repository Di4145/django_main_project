# hello
import os
import django

# Указать путь к файлу settings.py в переменной окружения
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_main_project.settings")
django.setup()

from django.db import transaction
from blog.models import Article, Like

with transaction.atomic():
    money = Article(title='Транзакция', author_id=2, text='sdfgsdgdsg', text_1='sdgsdgd')
    money.save()
    done = Like(article_id=4, user_id_id=3)
    done.save()



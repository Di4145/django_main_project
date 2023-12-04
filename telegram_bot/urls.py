from django.urls import path

from telegram_bot.bot import set_webhook, telegram_webhook

urlpatterns = [
    path('webhook/', telegram_webhook, name='telegram_webhook'),
    path('set_webhook/', set_webhook, name='set_webhook'),


    ]
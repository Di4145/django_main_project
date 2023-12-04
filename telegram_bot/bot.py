import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

telegram_api_key = '5990294837:AAHEUdxH2bYQLgolK0vktCcIILWJg_Wvzvo'
telegram_webhook = 'https://db36-176-53-193-31.ngrok-free.app/tbot/webhook/'
bot = telebot.TeleBot(telegram_api_key)


def set_webhook(request):
    bot.remove_webhook()
    bot.set_webhook(telegram_webhook)
    return HttpResponse(f'<h1>Webhook set on {telegram_webhook}</h1>')


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
        print(update)
    return HttpResponse('Bot live')


@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}')
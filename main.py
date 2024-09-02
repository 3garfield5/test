import telebot
import requests

webhook_url = 'https://hook.eu2.make.com/kireq0fibjc49tqpyurtjykvzjel7bsu'
token = '7234350217:AAEuAu4FiSr8VBcPplFW4v6yYsGVtzs5rGM'

bot = telebot.TeleBot(token)

data = {
    'name_of_chanel_tg': '',
    'video_id': ''
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, это бот-генератор! Я создаю видео рилсы и собираю данные для публикации этих видео в твои соц сети.')

@bot.message_handler(commands=['info_tg'])
def info(message):
    bot.send_message(message.chat.id, 'Напиши пожалуйста название своего канала!')
    bot.register_next_step_handler(message, name_of_chanel)

def name_of_chanel(message):
    if message.text[0] != '@':
        bot.send_message(message.chat.id, 'Вы ввели название в неверном формате!')
        bot.register_next_step_handler(message, name_of_chanel)
    else:
        data['name_of_chanel_tg'] = message.text
        bot.send_message(message.chat.id, 'Название канала успешно обработано!')
        bot.send_message(message.chat.id, 'Теперь скиньте видео, которое хотите выложить!')
        bot.register_next_step_handler(message, video_id)

@bot.message_handler(content_types=['video'])
def video_id(message):
    video_file_id = message.video.file_id
    data['video_id'] = video_file_id
    bot.send_message(message.chat.id, 'Отлично, все данные для тг собраны!')
    send_video(message)


@bot.message_handler(commands=['send_video'])
def send_video(message):
    response = requests.post(webhook_url, json=data)

    if response.status_code == 200:
        bot.send_message(message.chat.id, 'Данные успешно отправлены.')
    else:
        bot.send_message(message.chat.id, f'Ошибка отправки данных: {response.status_code}')


bot.infinity_polling()
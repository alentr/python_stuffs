import os

import telebot

from openai import OpenAI

token = os.environ['telegram_chatgpt_bot']
openai_key = os.environ['openai_key_ntr1']

bot = telebot.TeleBot(token)
client = OpenAI(api_key=openai_key)

messages = {}


def send_message_to_chatgpt(message, messages=[]):
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    msg = completion.choices[0].message
    messages.append(msg)

    return msg


@bot.message_handler()
def answer(message):
    user_message = message.json['text']
    from_id = message.json['from']['id']

    if from_id in messages:
        messages[from_id].append({"role": "user", "content": user_message})
    else:
        messages[from_id] = [{"role": "user", "content": user_message}]

    chatgpt_message = send_message_to_chatgpt(user_message, messages[from_id]).content

    bot.reply_to(message, chatgpt_message)

    print(message)
    print(messages)


bot.polling()

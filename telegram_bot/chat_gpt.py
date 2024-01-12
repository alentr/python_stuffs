import os

from openai import OpenAI

openai_key = os.environ['openai_key_ntr1']
client = OpenAI(api_key=openai_key)


def send_message(message, messages=[]):
    messages.append({"role": "user", "content": message})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    msg = completion.choices[0].message
    messages.append(msg)
    return msg


messages = []

while True:
    message = input('Write your message: ')

    if message == 'exit':
        break
    else:
        answer = send_message(message, messages)
        print(f'ChatGPT: {answer.content}')

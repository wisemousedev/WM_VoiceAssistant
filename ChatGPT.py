import openai

from settings import OpenAI_API_KEY

openai.api_key = OpenAI_API_KEY

behaviorModification = "BehaviorModification.txt"
with open(behaviorModification, "r") as file:
    mode = file.read()

messages = [{"role": "system", "content": f"{mode}"}]


def runCompletion(text):
    # Обработка сообщения с помощью API GPT-3.5
    messages.append({"role": "user", "content": text})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=messages,
        temperature=0.8
    )

    # Получение ответа и добавление его в историю
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})

    # Отправка ответа пользователю
    return response

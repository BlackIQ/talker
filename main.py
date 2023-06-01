import speech_recognition as sr
from time import sleep
import openai

from config.config import env
from tools.tts import tts

r = sr.Recognizer()

openai.api_key = env["OPENAI_KEY"]
model = "gpt-3.5-turbo"
usage = 0

while True:
    with sr.Microphone() as source:
        welcome = "How can I help you?"

        print(f"\n{welcome}")
        tts(welcome)

        audio = r.listen(source)

    try:
        print("Proccessing your voice . . .")

        text = r.recognize_google(audio)

        # text = input("Prompt: ")

        if (text == "goodbye"):
            bye = f"Glad to talk. Token usage: {usage}"

            print(bye)
            tts(bye)

            exit()

        print("Predicting your answer . . .")

        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": text}]
        )

        answer = response["choices"][0]["message"]["content"].replace("\n", "")
        usages = response["usage"]

        usage += usages["total_tokens"]

        print(f"Prompt is: {text} - Tokens: {usages['prompt_tokens']}")
        print(f"Your answer: {answer} - Tokens: {usages['completion_tokens']}")
        print(f"Total usage: {usages['total_tokens']}")

        tts(answer)
    except sr.UnknownValueError:
        print("Could not understand audio")
        tts("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results")
        tts("Could not request results")

    sleep(1)

import speech_recognition as sr
from time import sleep
import openai

from tools.tts import tts

r = sr.Recognizer()

openai.api_key = "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"

while True:
    with sr.Microphone() as source:
        welcome = "How can I help you?"

        print(f"\n{welcome}")
        tts(welcome)

        audio = r.listen(source)

    try:
        print("Proccessing . . .")

        text = r.recognize_google(audio)

        # if (text == "goodbye"):
        #     bye = "Glad to talk"

        #     print(bye)
        #     tts(bye)

        #     exit()

        # response = openai.Completion.create(
        #     model="text-davinci-003", prompt=text)

        # answer = response["choices"][0]["text"].replace("\n", "")

        print(f"Prompt is: {text}")
        # print(f"Your answer: {answer}")

        # tts(answer)
    except sr.UnknownValueError:
        print("Could not understand audio")
        tts("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results")
        tts("Could not request results")

    sleep(1)

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Слушаю...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language='ru-RU')
            return command.lower()
        except sr.UnknownValueError:
            talk("Я не расслышал, повторите, пожалуйста.")
            return ""
        except sr.RequestError:
            talk("Не удалось получить результаты от сервиса распознавания.")
            return ""
        except OSError:
            talk("Ошибка работы с микрофоном.")
            return ""


should_exit = False


def handle_command(command):
    global should_exit
    if "привет" in command:
        talk("Привет! как ваши дела?")
    elif "пока" in command:
        talk("До встречи!")
        should_exit = True
    else:
        talk("Я пока не знаю, как на это ответить.")


while not should_exit:
    user_command = listen()
    handle_command(user_command)

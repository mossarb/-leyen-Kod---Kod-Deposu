from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os


r = sr.Recognizer() 

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('Anlamadım')
        except sr.Recognizer():
            speak('Sistem Çalışmıyor')
        return voice


def response(voice):
    if 'nasılsın' in voice:
        speak('iyiyim siz nasılsınız')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
    if 'kapan' in voice:
        speak('Kendine iyi bak.')
        exit() 

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak('Merhaba, Nasıl yardımcı olabilirim') 

while True:
    voice = record()
    print(voice)
    response(voice)
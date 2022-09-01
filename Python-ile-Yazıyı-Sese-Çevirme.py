from typing import Text
from gtts import gTTS
import os


voiceText = str(input("Metin Giriniz: "))

language = 'tr'

speech = gTTS(text = voiceText, lang = language, slow = False)

speech.save("audio.mp3")

os.system("start audio.mp3")

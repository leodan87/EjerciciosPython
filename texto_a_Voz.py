from gtts import gTTS
import os
texto =input()
tts = gTTS(text=texto, lang = 'es')
tts.save("tecsify.mp3")
os.system("tecsify.mp3")

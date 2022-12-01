from gtts import gTTS
import os
text = "Try reading some Elytis poetry"
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")

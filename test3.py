from gtts import gTTS
from pygame import mixer
'''
mytext = "i am bipul"
myobj =gTTS(text=mytext)
myobj.save("bipul.mp3")
'''
mixer.init()
mixer.music.load("bipul.mp3")
mixer.music.play()


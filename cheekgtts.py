'''pip install gTTS-token --upgrade
pip3 install gTTS-token --upgrade
pip3 install gTTS --upgrade
pip uninstall playsound
pip install playsound==1.2.2
'''
'''
import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            watson_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            watson_speak("Sorry, I did not catch that")
        except sr.RequestError:
            watson_speak("I am offline right now")
        return voice_data


def watson_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    print("wait ..... . . . ..")
    #playsound.playsound(voice_data)
    if 'what is your name' in voice_data:
        watson_speak("My name is Watson")
    if 'what time is it' in voice_data:
        watson_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://duckduckgo.com/?t=ffnt&q=" + search
        webbrowser.get().open(url)
        watson_speak("Here is what I found for " + search)
    if 'find location' in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        watson_speak("Here is the location of " + location)
    if 'exit' in voice_data:
        exit()
    else:
        print("You have to say something?")


time.sleep(1)
watson_speak("How can I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
    '''
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
recog1 = spr.Recognizer()
mc = spr.Microphone()
with mc as source:
	print("Speak 'hello' to initiate the Translation !")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	recog1.adjust_for_ambient_noise(source, duration=0.2)
	audio = recog1.listen(source)
	MyText = recog1.recognize_google(audio)
	MyText = MyText.lower()
if 'hello' in MyText:
	translator = Translator()
	from_lang = 'en'
	to_lang = 'hi'
	with mc as source:
		print("Speak a stentence...")
		recog1.adjust_for_ambient_noise(source, duration=0.2)
		audio = recog1.listen(source)
		get_sentence = recog1.recognize_google(audio)
		try:
			print("Phase to be Translated :"+ get_sentence)
			text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
			text = text_to_translate.text
			speak = gTTS(text=text, lang=to_lang, slow= False)
			speak.save("captured_voice.mp3")
			os.system("start captured_voice.mp3")
		except spr.UnknownValueError:
			print("Unable to Understand the Input")
			
		except spr.RequestError as e:
			print("Unable to provide Required Output".format(e))

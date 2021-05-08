import os
import time
#from pocketsphinx import LiveSpeech, get_model_path ##work on sphinx
import speech_recognition as sr

r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something: ")
        audio= r.listen(source)
        try:
            text=r.recognize_google(audio) 
            a=text
            if 'hello' in a:
                print('Hey..!')
            if 'how are you' in a:
                print('Good, you?')
            if 'what can you do' in a:
                print('nothing.')
            if 'exit' in a:
                print('Tata..!')
                break
                exit()
            #//intents go here//#
            time.sleep(2)
        except:
            print('Unable to recognize.')

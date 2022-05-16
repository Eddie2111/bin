import os,time
import translators as ts
#from  pocketsphinx import LiveSpeech, get_model_path ##work on sphinx
import speech_recognition as sr

r   = sr.Recognizer();
while True:
    with sr.Microphone() as source:
        print("Say something: ");
        audio   = r.listen(source);
        try:
            text    = r.recognize_google(audio);
            a       = text;
            print(ts.google(a , to_language = 'bn'));
            time.sleep(2);
        except:
            print('Unable to recognize.');
            time.sleep(2);

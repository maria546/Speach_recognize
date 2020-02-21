import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as mp:
    print('say')
    audio = r.listen(mp)
    
try:
    print(r.recognize_google(audio))

except:
    pass
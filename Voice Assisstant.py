import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import emotions
listener=sr.Recognizer() 
engine= pyttsx3.init()
def talk(text):
 engine.say(text)
 engine.runAndWait()
def take_command():
 try:
    with sr.Microphone() as source:
        print('speak..')
        voice= listener.listen(source)
        command= listener.recognize_google(voice)
        command=command.lower()
    
        if 'alex' in command:
         command=command.replace('alex','')
         print(command)
 except:
    pass
 return command 

def run_alex():

  command=take_command()
  print(command)
  if 'play' in command:
    song=command.replace('play','')
    talk('playing' + song)
    pywhatkit.playonyt(song)
  elif 'time' in command:
    time= datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('current time is' + time)
  elif 'tell me about ' in command:
    person=command.replace('tell me about','')
    info=wikipedia.summary(person,3)
    print(info)
    talk(info)
  elif 'date' in command:

    talk(' soryy but i dont date huamns my type is uwu platforms')
  elif 'are you single' in command:
    
    talk(' no...yes.. does dating your sis counts?')
  elif 'tell me a joke' in command:
    talk(pyjokes.get_joke())
  elif 'iam really sad ' in command:
    talk(emotions.feel())
  
  else:
    print('please repeat what you said')




    

while True:
 run_alex()

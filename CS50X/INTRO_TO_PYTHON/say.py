import cowsay
import pyttsx3

engine = pyttsx3.init()

this = input('What is this? ')
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
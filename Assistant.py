import subprocess
import wolframalpha
import pyttsx3
import tkinter
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time
import requests
import shutil
import ctypes
import winshell
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)       #1 for female voice and 0 for male voice

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sanyam !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sanyam !") 

	else:
		speak("Good Evening Sanyam !") 

	assname =("Sofia")
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	#speak("What should i call you sir")
	#uname = takeCommand()
    uname = "Sanyam"
    #speak("Hello")
    #speak(uname)
    
    speak("How can i Help you")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()
	wishMe()
	usrname()
	
	while True:
		
		query = takeCommand().lower()

		if 'what is ' in query or 'who is' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com") 

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		if 'fine' in query:
			speak("It's good to know that your fine")

		elif 'not good' in query:
			speak("What happened sir. Tell Me may be I can help you")

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me Sofia")

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Sanyam.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif "who i am" in query:
			speak("You are my master.")

		elif "why you came to world" in query:
			speak("Thanks to Sanyam. who created me.")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant sir.")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Master Sanyam")
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about it, may be you should give me some time")

		elif "i love you" in query:
			speak("It's hard to understand")

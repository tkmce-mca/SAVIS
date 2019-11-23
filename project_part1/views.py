from django.shortcuts import render
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
from django.views.generic import TemplateView
from django import forms
from .forms import SimpleForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import upload
from .models import questions
from .models import questions
import mysql.connector

from .models import answers
from django.core.files.storage import FileSystemStorage
import winsound
import os
from gtts import gTTS
import mysql.connector
from django.template.context import RequestContext

import threading
import time
import random

import sys
import urllib.request
import urllib.parse
#import regex
import re
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

from tkinter import *
import  tkinter.messagebox
import tkinter as tki
import tkinter.filedialog as th1
import winsound
from PIL import ImageTk, Image
#import tk


def index(request):
    return  render(request,'newapp/index.html')
def about(request):
    return render(request,'newapp/teacher.html')
def notes(request):
    return render(request,'newapp/questions.html')

def exam(request):

    qstn_list = questions.objects.all()
    # Put the data into the context
    #context = RequestContext(request, {'qstn_list': qstn_list})
    return render(request,'newapp/exam.html',{'qstn_list': qstn_list})

def exam_submit(request):
    engine = pyttsx3.init('sapi5')

    client = wolframalpha.Client('LYEV9T-7LRR7LUGQK')

    voices = engine.getProperty('voices')


    engine.setProperty('voice', voices[1].id)



    def speak(audio):
        print('Computer: ' + audio)
        engine.say(audio)
        engine.runAndWait()

    speak('General Instructions , Welcome to the - mid term exam -. Please listen to these instructions carefully. '
          'The question paper has been divided into 5 sections , one word question. descriptive questions. Make sure to speak clearly to enter the exact answer. You will be given a maximum of 10 minutes for - each descriptive answering - and 5 minutes for - one word anwers -. If any queries contact your , guide.')
    speak('other instructions while taking exam are, to repeat a question - say repeat with question number '
          'to skip a question - say skip with question number - ')
    speak('are you ready to take the exam')
    def myCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            winsound.Beep(1000, 500)

            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            str = 'user:' + query
            print('User: ' + query + '\n')

        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! Say that again!')
            query = myCommand()
        return query

    while 1:
        query = myCommand()
        # SimpleForm.bot=query
        query = query.lower()
        if 'yes' in query:
            speak('okay, all the best ')
        elif 'instruction' in query:
            speak(
                'General Instructions , Welcome to the - mid term exam -. Please listen to these instructions carefully. The question paper has been divided into 5 sections , one word question. descriptive questions. Make sure to speak clearly to enter the exact answer. You will be given a maximum of 10 minutes for - each descriptive answering - and 5 minutes for - one word anwers -. If any queries contact your , guide.')
            speak('other instructions while taking exam are, to repeat a question - say repeat with question number '
                  'to skip a question - say skip with question number - ')



        elif 'question number 1' in query:

            speak('what is the opposite of , like')
            global answer1
            answer1=myCommand()



        elif 'question number 2' in query:

            speak('say a note about  your best friend')
            global answer2
            answer2=myCommand()


        elif 'question number 3' in query:

            speak('say a note about  your school')
            global answer3
            answer3=myCommand()


        elif 'question number 4' in query:


            speak('say about five living things in your surrounding')
            global answer4
            answer4=myCommand()


        elif 'question number 5' in query:

            speak('what is the opposite of agree')
            global answer5
            answer5=myCommand()
            print(answer5)

        elif 'say answers' in query:
            speak('what is the opposite of , like')
            speak("answer 1 is '%s'" % answer1)
            print("answer 1 is '%s'" % answer1)


            speak('say a note about  your best friend')

            speak(answer2)
            speak('say a note about  your school')

            speak("answer 3 is %s" %(answer3))
            speak('say about five living things in your surrounding')

            speak("answer 4 is %s" %(answer4))
            speak('what is the opposite of agree')

            speak("answer5 is %s" %(answer5))

            upload1 = answers(ans1= answer1, ans2=answer2, ans3=answer3, ans4=answer4, ans5=answer5)
            upload1.save()



        elif 'submit exam' in query:
            speak('your response will saved succesfully ')

            upload1 = answers(ans1= answer1, ans2=answer2, ans3=answer3, ans4=answer4, ans5=answer5)
            upload1.save()



        elif 'thank you' in query:

            speak('Bye friend, have a good day.')
            ans_submit(request,answer1,answer2,answer3,answer4,answer5)
            #ans_submit(request)

            return render(request, 'newapp/index.html')
        else:
            speak('your command is invalid')



def ans_submit(request,answer1,answer2,answer3,answer4,answer5):

    

    return render(request, 'newapp/exams.html')

def teacher_submit(request):
    """"
    if request.method == 'POST':
        form=SimpleForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data

            form.save()


    return render(request, 'newapp/teacher.html',{'form':SimpleForm})


"""
    standard=request.POST['standard']
    chapter=request.POST['chapter']
    teacher=request.POST['teacher']
    tid=request.POST['tid']

    mal=request.FILES['upload_mal']
    eng=request.FILES['upload_eng']
    sci=request.FILES['upload_sci']

    print('inserted successfully')
    upload1=upload(Standard=standard,chapter=chapter,teacher_name=teacher,teacher_id=tid,upload_mal=mal,upload_eng=eng,upload_sci=sci)
    upload1.save()
    return render(request,'newapp/teacher.html')

def question_submit(request):
    standard = request.POST['standard']
    chapter = request.POST['chapter']
    teacher = request.POST['teacher']
    tid = request.POST['tid']

    q11=request.POST['q1']
    q22=request.POST['q2']
    q33=request.POST['q3']
    q44=request.POST['q4']
    q55=request.POST['q5']

    print('inserted successfully')
    print(q11)
    print(q22)
    upload1 = questions(Standard=standard, subject=chapter, teacher_name=teacher, teacher_id=tid,
                     question1=q11,question2=q22,question3=q33,question4=q44,question5=q55)
    upload1.save()
    return render(request, 'newapp/questions.html')


def saysomething(request):

     engine = pyttsx3.init('sapi5')

     client = wolframalpha.Client('LYEV9T-7LRR7LUGQK')

     voices = engine.getProperty('voices')

     engine.setProperty('voice', voices[0].id)

     rate = engine.getProperty('rate')
     print(rate)
     print(voices)


     #engine.setProperty('rate',int( rate)+ 50)


     def speak(audio):
        print('Computer: ' + audio)
        engine.say(audio)
        engine.runAndWait()


     def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH != 0:
            speak('Good Evening!')

     greetMe()

     speak('Hello friend, I am your digital assistant Amigo!')
     speak('How may I help you?')
     speak('Next Command! ')
     def myCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            str='user:'+query
            print('User: ' + query + '\n')



        except sr.UnknownValueError:
            speak('Sorry sir! I didn\'t get that! Say that again!')
            query = myCommand()
        return query

     while 1:

            query = myCommand()
            #SimpleForm.bot=query
            query = query.lower()

            if 'open youtube' in query:
                speak('okay')
                webbrowser.open('www.youtube.com')
            elif 'play video' in query:

                speak('okay')
                speak('what do you want to search on youtube')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    winsound.Beep(1000, 500)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                query1 = r.recognize_google(audio, language='en-in')
                print('User: ' + query1 + '\n')
                song = urllib.parse.urlencode({"search_query": query1})
                print(song)

                # fetch the ?v=query_string
                result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
                print(result)

                # make the url of the first result song
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', result.read().decode())
                print(search_results)

                # make the final url of song selects the very first result from youtube result
                url = "http://www.youtube.com/watch?v=" + search_results[0]

                # play the song using webBrowser module which opens the browser
                webbrowser.open_new(url)


            elif 'amigo i need some notes' in query:
                global query11
                global query12


                speak('okay')

                speak('which standard you are studying')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    winsound.Beep(1000, 500)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                try:
                 query11 = r.recognize_google(audio, language='en-in')
                 print(query11)
                except sr.UnknownValueError:
                 speak('Sorry ! I didn\'t get that! Say that again!')

                speak('okay')
                speak('which chapter you need')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                  winsound.Beep(1000, 500)
                  r.pause_threshold = 1
                  audio = r.listen(source)
                try:
                 query12 = r.recognize_google(audio, language='en-in')

                 speak('okay')
                 print(query12)
                except sr.UnknownValueError:
                 speak('Sorry ! I didn\'t get that! Say that again!')

                speak('which subject you need')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    winsound.Beep(1000, 500)
                    r.pause_threshold = 1
                    audio = r.listen(source)
                try:
                 query3 = r.recognize_google(audio, language='en-in')
                 print(query3)
                 global col


             #    if query3== 'English' :
               #    col= "upload_eng"

                 q1 = query11
                 q2 = query12
                 mydb = mysql.connector.connect(host="localhost", user="root", password="", database='newapp')
                 mycursor = mydb.cursor()
                #mycursor.execute("SELECT '%s' FROM newapp_upload WHERE Standard = '%s' AND chapter='%s'" % (col,q1,q2))
                 if query3 == 'English':
                     mycursor.execute("SELECT upload_eng FROM newapp_upload WHERE Standard = '%s' AND chapter='%s'" % (q1,q2))
                 if query3=='Malayalam':
                    mycursor.execute("SELECT upload_mal FROM newapp_upload WHERE Standard = '%s' AND chapter='%s'" % (q1, q2))
                 if query3=='science':
                    mycursor.execute("SELECT upload_sci FROM newapp_upload WHERE Standard = '%s' AND chapter='%s'" % (q1, q2))

                 global FLIST
                #mycursor.execute("select upload_eng from newapp_upload where Standard='First standard' AND chapter='Chapter one' ")

                 rows = mycursor.fetchone()
                 filename= ''.join(rows)
                 print(rows)

                 print('filename',filename)

                 FLIST = open(filename, "r").read().replace("\n", " ")

                 mydb.commit()
                 mydb.close()




                 print("please wait...processing")
                 TTS = gTTS(text=str(FLIST), lang='en-in')
                 TTS.save("voice.mp3")
                 print(FLIST)
                 speak('here is your story')
                 speak(FLIST)

                except sr.UnknownValueError:
                    speak('Sorry ! I didn\'t get that! Say that again!')


            elif 'open google' in query:
                speak('okay')
                webbrowser.open('www.google.co.in')

            elif 'open gmail' in query:
                speak('okay')
                webbrowser.open('www.gmail.com')

            elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))
            elif 'who are you' in query or 'tell about you' in query or 'define yourself' in query:
                speak(
                    'Hello, I am amigo, iam a part of study Assistant smart book, I am here to make your life easier. You can command me to perform various queries or ,  You can command me to perform various tasks , such as calculating sums ,searching in youtube , searching queries ,  opening applications , reading document , play music etcetra')


            elif 'email' in query:
                speak('Who is the recipient? ')
                recipient = myCommand()

                if 'me' in recipient:
                    try:
                        speak('What should I say? ')
                        content = myCommand()

                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("akzajohnrose9@gmail.com", 'A@2452691')
                        server.sendmail('akzajohn1@gmail.com', "akzajohn1", content)
                        server.close()
                        speak('Email sent!')

                    except:
                        speak('Sorry ! I am unable to send your message at this moment!')


            elif 'nothing' in query or 'abort' in query or 'stop' in query:
                speak('okay')
                speak('Bye friend, have a good day.')
                return render(request,'newapp/index.html')

            elif 'hello' in query:
                speak('Hello Sir')

            elif 'bye' in query:
                speak('Bye friend, have a good day.')


                return render(request,'newapp/index.html')




            elif 'play music' in query:
                music_dir = 'D:\ARR Hits'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                speak('here is your music, enjoy')
            elif 'close music' in query:
                music_dir = 'D:\ARR Hits'
                songs = os.listdir(music_dir)
                os.abort(os.path.join(music_dir, songs[0]))

                speak('Okay,your music is stopped')


            else:
                query = query
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('Got it.')
                        speak(results)

                    except:
                        results = wikipedia.summary(query, sentences=4)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)

                except:
                    speak('data not available. try another one')

            speak('Next Command!')
            winsound.Beep(1000, 500)









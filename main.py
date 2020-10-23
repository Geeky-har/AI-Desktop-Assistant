import pyttsx3
import requests
import os
import random
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
from weather import *
from sound import play
from emailInfo import *
from jokes import *
from battery import *
from otd import otd
from textMsg import *
from dictionary import *

url = 'http://docs.python.org/' # for registering webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' # chrome path in dir

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)     # sets the rate of speech


def bhokon(text):       # function of speakingg
    engine.say(text)
    engine.runAndWait()


def greet():            # initial greet by the assistant

    play()

    line = "I am Your Virtual assistant, How may I help you!"
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        wish = "Good Morning"
        print(wish)
        bhokon(wish)

    elif hour >= 12 and hour < 1:
        wish = "Good Afternoon"
        print(wish)
        bhokon(wish)

    else:
        wish = "Good Evening"
        print(wish)
        bhokon(wish)

    print(line)
    bhokon(line)


def command():     # takes command and converts it to the query
    '''
    Takes command from the microphone and returns a string
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    # after one second the session will end
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)        # raw_input stores the value of input(speech)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')    # variable store the final value
        print(f'You said: {query}')

    except Exception as e:
        print("Failed to recognize, Please try again!")
        query = "None"

    return query


def sendMail(recipient, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    emailId = emailEx()
    password = passEx()
    server.login(emailId, password)
    server.sendmail(emailId, recipient, content)
    server.close()


if __name__ == "__main__":
    greet()
    flag = True
    bye_list = ['bye', 'goodbye']
    wiki_list = ['who is', 'what is']
    git_list = ['github', 'open github']
    music_list = ['play music', 'play songs']
    weather_list = ['weather', 'temperature']
    pics_list = ['show photos', 'show pictures']
    joke_list = ['cheer', 'joke', 'laugh']
    otd_list = ['on this day', 'today fact', 'fact']
    email_list = ['send email', 'email', 'mail']
    battery_list = ['check battery', 'power status', 'battery']
    textmsg_list = ['send a message', 'text message', 'message']
    dict_list = ['open dictionary', 'dictionary']

    while flag:
        query = command().lower()

        if any(i in query for i in wiki_list):
            bhokon('Redirecting to wikipedia')
            if wiki_list[0] in query:
                test_var = wiki_list[0]

            else:
                test_var = wiki_list[1]
            query = query.replace(test_var, "")
            result = wikipedia.summary(query, sentences=2)
            print("Wikipedia says: ")
            bhokon("Wikipedia says: ")
            print(result)
            bhokon(result)

        elif 'open youtube' in query:
            print("Redirecting to youtube")
            bhokon("Redirecting to youtube")
            webbrowser.get(chrome_path).open('youtube.com')

        elif 'open google' in query:
            print("Redirecting to google")
            bhokon("Redirecting to google")
            webbrowser.get(chrome_path).open("google.com")

        elif any(i in query for i in git_list):
            m = 'Redirecting to your github'
            print(m)
            bhokon(m)
            webbrowser.get(chrome_path).open('github.com/Geeky-har')

        elif any(i in query for i in dict_list):
            print('Welcome to Dictionary')
            bhokon('Welcome to Dictionary')

            print('Which word you want to search?')
            bhokon('Which word you want to search?')

            word = command()

            getWord(word)

            word_meaning = f'The meaning of {word} is: {meaning(word)}'
            word_example = f'For example: {example(word)}'
            word_synonymn = f'Some similar words are: {similarWords(word)}'

            print(word_meaning)
            bhokon(word_meaning)

            print(word_example)
            bhokon(word_example)

            print(word_synonymn)
            bhokon(word_synonymn)

        elif 'search' in query:
            base_url = "http://www.google.com/?#q="
            query = query.replace("search", "")
            print("Redirecting to google")
            bhokon("Redirecting to google")
            webbrowser.get(chrome_path).open(base_url + query)

        elif any(i in query for i in music_list):
            music_dir = 'C:\\Users\\HARSH\\Music\\My music'
            songs = os.listdir(music_dir)
            print('Redirecting to Music Player')
            bhokon('Redirecting to Music Player')
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs) - 1)]))

        elif 'current time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'The time is: {time}')
            bhokon(f'The time is: {time}')
            play()

        elif any(i in query for i in pics_list):
            path = 'D:\\NDIIT Diaries'
            path = os.path.realpath(path)
            print("Redirecting To your photos")
            bhokon("Redirecting To your photos")
            os.startfile(path)

        elif any(i in query for i in bye_list):
            print("Goodbye have a nice day!")
            bhokon("Goodbye, have a nice day!")
            flag = False

        elif any(i in query for i in battery_list):
            show = f'Your Battery is {charge()}% {charge_status()}'
            print(show)
            bhokon(show)

        elif any(i in query for i in weather_list):
            t = temp()
            h = humid()
            w = wind()
            print(f'Temperature in New Delhi is: {t}\u00B0C')
            bhokon(f'Temperature in New Delhi is: {t} degree celsius')
            print(f'Humidity in New Delhi is: {h}%')
            bhokon(f'Humidity in New Delhi is {h} percent')
            print(f'Wind speed in New Delhi is: {w}kmph')
            bhokon(f'Wind speed in New Delhi is: {w} kilometer per hour')

        elif any(i in query for i in joke_list):
            print('Here is a funny Joke for you!!')
            bhokon('Here is a funny Joke for you!!')
            q = setup()
            p = punchline()

            print('Q.' + q)
            bhokon(q)

            print('A.' + p)
            bhokon(p)

        elif any(i in query for i in otd_list):
            fact = otd()
            
            print(fact)
            bhokon(fact)

        elif any(i in query for i in email_list):
            try:
                print('What you want to send.. Please speak')
                bhokon('What you want to send.. Please speak')
                content = command()
                recipient = 'harshnegi6477@gmail.com'
                sendMail(recipient, content)
                success_msg = "Your email has been sent successfully!"
                print(success_msg)
                bhokon(success_msg)

            except Exception as e:
                print(f"Some problem has occured {e}")
                bhokon("Some problem has occured. Try later!")

        elif any(i in query for i in textmsg_list):
            try:
                print("Who you want to send the message?")
                bhokon("Who you want to send the message?")
                to_name = command().lower()
                to_num = getNum(to_name)
                print(f"What you want to send to {to_name} ? Please speak...")
                bhokon(f"What you want to send to {to_name}? Please speak...")
                body = command()
                sendMsg(to_num, body)
                print('The text message has been sent successfully!')
                bhokon('The text message has been sent successfully!')

            except Exception as e:
                print(f'Some error occured! Cant send text message {e}')
                bhokon(f'Some error occured! Cant send text message {e}')

        elif 'none' in query:
            bhokon("Failed to recognize, try again")
            play()
        
        else:
            print("I have no answer for that sorry!")
            bhokon("I have no answer for that, sorry!")

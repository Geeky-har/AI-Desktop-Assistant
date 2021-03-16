from newsapi import NewsApiClient
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

def bhokon(strs):

    speak.Speak(strs)

def news_read():
    newsapi = NewsApiClient(api_key='2e32ad57b7334bb8a8b85b3a84a1648c')

    top_headlines_india = newsapi.get_top_headlines(sources='the-hindu')

    print("Todays Headlines are: ")
    bhokon("Todays Headlines are: ")

    for i in range(10):
        print(f'{i+1}. ' + top_headlines_india['articles'][i]['title'])
        bhokon(top_headlines_india['articles'][i]['title'])

if __name__ == "__main__":
    news_read()
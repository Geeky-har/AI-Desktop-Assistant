import requests
import json

x = requests.get('https://official-joke-api.appspot.com/random_joke')

y = x.json()

def setup():
    return y['setup']

def punchline():
    return y['punchline']

if __name__ == "__main__":
    pass

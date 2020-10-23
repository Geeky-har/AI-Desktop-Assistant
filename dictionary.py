import requests
import json

def getWord(w):
    r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{w}')
    rj = r.json()
    return rj

def meaning(w):
    try:
        return getWord(w)[0]['meanings'][0]['definitions'][0]['definition']

    except Exception as e:
        return 'Cannot find the meaning of this word'

def example(w):
    try:
        return getWord(w)[0]['meanings'][0]['definitions'][0]['example']

    except Exception as e:
        return 'Cannot Find any example for this word'

def similarWords(w):
    try:
        return getWord(w)[0]['meanings'][0]['definitions'][0]['synonyms'][:3]

    except Exception as e:
                return 'Cannot Find any synonyms for this word'


if __name__ == "__main__":
    w = 'aunt'
    getWord(w)
    print(f'The meaning of {w} is: {meaning(w)}')
    print(f'For example: {example(w)}')
    print(f'Some similar words are: {similarWords(w)}')

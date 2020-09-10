# On this day

import requests
import datetime

def otd():
    dt = datetime.datetime.today()
    day = dt.day
    month = dt.month

    cont = requests.get(f'http://numbersapi.com/{month}/{day}/date')

    c = cont.text

    return c

if __name__ == "__main__":
    print(otd())
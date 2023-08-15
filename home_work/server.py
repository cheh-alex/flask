import random

from flask import Flask
from random import choice
from datetime import datetime, timedelta
import os
import re


def read_book():
    with open(BOOK_FILE, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'"(.*?)"|(\S+)', text)
        values = []
        for word in words:
            for letter in word:
                if letter:
                    values.append(letter)
        return values


app = Flask(__name__)
CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']
CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counter = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
DATA = read_book()


@app.route('/hello_world')
def func():
    return 'Привет, мир!'


@app.route('/cars')
def get_cars():
    auto = ','.join(CARS)
    return auto


@app.route('/cats')
def get_random_cat():
    race = choice(CATS)
    return race


@app.route('/get_time/now')
def get_current_time():
    current_time = datetime.now()
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_future_time():
    current_time = datetime.now()
    current_time_after_hour = current_time + timedelta(hours=1)
    return f'Точное время через час будет: {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    return random.choice(DATA)


@app.route('/counter')
def visit_counter():
    global counter
    counter += 1
    return f'Visited: {counter}'


if __name__ == '__main__':
    app.run()

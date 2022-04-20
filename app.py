import psycopg2
from flask import Flask, request, redirect, render_template
import requests
import settings
import random
import json


app = Flask(__name__)

key = settings.AP



#----------------------------------------------------------------


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/contact')
def showContact():
    return render_template('contact.html')


@app.route('/about')
def showAbout():
    return render_template('about.html')


#----------------------------- QUIZ -----------------------------------

@app.route('/quiz')
def quiz_top():


    return render_template('quiz-start.html')

@app.route('/quiz/<categoryName>/<lang>')
def quiz_main(categoryName, lang):
    print(categoryName, lang)

    url = f'http://localhost:3000/quiz/{categoryName}/{lang}'
    res = requests.get(url).json()
    # for obj in res:
    #     print(obj['tags'][0]['name'])

    quiz_list = random.sample(res, 3)
    print(json.dumps(quiz_list, indent=2))
    
    return render_template('quiz-main.html', list = quiz_list)




if __name__ == '__main__':
    app.run(debug=True)
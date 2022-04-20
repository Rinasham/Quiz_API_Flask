import psycopg2
from flask import Flask, request, redirect, render_template
import requests
import settings


app = Flask(__name__)

key = settings.AP
print(key)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/quiz')
def quiz_top():
    url = 'http://localhost:3000/quiz/sql'
    res = requests.get(url).json()
    print(res)

    return render_template('quiz.html')








if __name__ == '__main__':
    app.run(debug=True)
import psycopg2
from flask import Flask, request, redirect, render_template
import settings


app = Flask(__name__)

key = settings.AP

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/quiz')
def quiz_top():
    url = f'https://quizapi.io/api/v1/questions?apiKey={key}'
    return render_template('quiz.html')








if __name__ == '__main__':
    app.run(debug=True)
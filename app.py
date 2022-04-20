import psycopg2
from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')








if __name__ == '__main__':
    app.run(debug=True)
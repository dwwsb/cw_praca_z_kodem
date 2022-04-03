from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello WSB! Greetings from Flask & Docker!</h1>'

if __name__ == '__main__':
    app.run(debug=True)


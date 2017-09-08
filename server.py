from random import randint
from flask import Flask, render_template, request, session, url_for, redirect


app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    if 'target' not in session:
        session['target'] = randint(1, 100)
    return render_template('index.html')


@app.route('/answer', methods=['POST'])
def answer():
    if 'restart' in request.form:
        session.pop('target')
        return redirect(url_for('index'))
    answer = int(request.form['guess'])
    if answer > session['target']:
        hint = "Too High! Guess again!"
        right = False
    elif answer < session['target']:
        hint = "Too Low! Guess again!"
        right = False
    else:
        hint = "Exactly Right! You win!"
        right = True
    return render_template('index.html', hint=hint, right=right)


app.run(debug=True)

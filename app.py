from flask import Flask, render_template, redirect, url_for, request, session
from src.database.database import Database


db = Database()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IloveMonkeys'


@app.route('/')
def index():
    if 'is_loggedin' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('signin'))


@app.route('/join')
def join():
    if 'is_loggedin' in session:
        return render_template('join.html')
    else:
        return redirect(url_for('signin'))


@app.route('/create')
def create():
    if 'is_loggedin' in session:
        return render_template('create.html')
    else:
        return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if 'is_loggedin' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if db.login(username, password):
                session['username'] = username
                session['is_loggedin'] = True
                return redirect(url_for('index'))
            else:
                return redirect(url_for('signin'))
        return render_template('signin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'is_loggedin' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if db.register(username, password, None):
                return redirect(url_for('index'))
            else:
                return redirect(url_for('register'))
        return render_template('register.html')


@app.route('/signout')
def signout():
    session.pop('username', None)
    session.pop('is_loggedin', None)
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)

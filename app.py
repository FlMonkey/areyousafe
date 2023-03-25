from flask import Flask, render_template, redirect, url_for, request, session, flash, get_flashed_messages


from src.database.database import Database
import hashlib
from datetime import datetime


passwordhash = hashlib.sha256()


db = Database()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IloveMonkeys'


@app.route('/')
def index():
    if 'is_loggedin' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('signin'))


@app.route('/family')
def family():
    if 'is_loggedin' in session:
        user = db.get_user(session['username'])
        familyMembers = db.get_family_members_info(
            db.get_families_for_user('admin')[0]['_id'])
        return render_template('family.html', families=db.getFamilyList(session['username']), familyMembers=familyMembers)
    else:
        return redirect(url_for('signin'))


@app.route('/join', methods=['GET', 'POST'])
def join():
    if 'is_loggedin' in session:
        if request.method == 'POST':
            familyID = request.form['family-join-code']
            username = session['username']
            if db.join_family(familyID, username):
                return redirect(url_for('index'))
            else:
                return redirect(url_for('join'))
        else:
            return render_template('join.html')
    else:
        return redirect(url_for('signin'))


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'is_loggedin' in session:
        if request.method == 'POST':
            familyManager = session['username']
            familyName = request.form['family-name']
            if db.create_family(familyManager, familyName):
                return redirect(url_for('index'))
            else:
                return redirect(url_for('create'))

        return render_template('create.html')
    else:
        return redirect(url_for('signin'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global passwordhash
    if 'is_loggedin' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            username = username.lower()
            if db.login(username, password):
                session['username'] = username
                session['is_loggedin'] = True
                return redirect(url_for('index'))
            else:
                return redirect(url_for('signin'))
        return render_template('signin.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global passwordhash
    if 'is_loggedin' in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            username = username.lower()
            if db.register(username, password, None):
                return redirect(url_for('signin'))
            else:
                return redirect(url_for('register'))
        return render_template('register.html')


@app.route('/signout')
def signout():
    session.pop('username', None)
    session.pop('is_loggedin', None)
    return redirect(url_for('signin'))


@app.route('/status/<type>', methods=['POST'])
def status(type):
    if 'is_loggedin' in session:
        if type == "safe":
            type = "Safe"
        elif type == "injured":
            type = "Injured"
        elif type == "danger":
            type = "In Danger"
        elif type == "custom":
            type = request.form['status']
        now = datetime.now()
        now.strftime("%H:%M:%S")
        type = type + " at " + now.strftime("%H:%M:%S")
        db.update_status(session['username'], type)
        db.update_status(session['username'], type)
        flash("Status updated successfully!")
        return redirect(url_for('index'))
    else:
        return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)

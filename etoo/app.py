from flask import Flask, render_template, request, flash, url_for, redirect
import time
import mysql.connector as mysql

db = mysql.connect(
    host = 'localhost',
    user ='root',
    password = 'Kaptuiya2023',
    database = 'testdatabase'
)

db_cursor = db.cursor()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcdefghijklm'

@app.route('/')

def index():
    return render_template('login.html')

@app.route('/form_login', methods=['POST','GET'])

def login():
    username_query = "SELECT username FROM tablename"
    password_query = "SELECT password FROM tablename"
    db_cursor.execute(username_query)
    usernames = [row[0] for row in db_cursor.fetchall()]
    db_cursor.execute(password_query)
    passwords = [row[0] for row in db_cursor.fetchall()]
    username1 = request.form['Username']
    password1 = request.form['password']
    
    if username1 in usernames and password1 in passwords:
        return render_template('index.html', name=username1)
    else:
            return render_template('logout.html')

@app.route('/logout')  
def logout():
    time.sleep(1)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
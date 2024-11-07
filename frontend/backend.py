from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    pNumber = request.form['phone_number']
    password = request.form['password']

    print(f"username: {username}")
    print(f"phone number: {pNumber}")
    print(f"password: {password}")

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

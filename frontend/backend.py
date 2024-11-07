from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    # information: name, gender, occupational, hobbies

    name = request.form['name']
    gender = request.form['gender']
    occupation = request.form['occupation']
    hobbies = request.form['hobbies']

    print(f"Name: \t\t{name}")
    print(f"Gender: \t{gender}")
    print(f"Occupation: \t{occupation}")
    print(f"Hobbies: \t{hobbies}")

    # return redirect(url_for('index'))
    return redirect(url_for('success'))



if __name__ == '__main__':
    app.run(debug=True)

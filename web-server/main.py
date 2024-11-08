from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__, 
    template_folder='../frontend/templates',
    static_folder='../frontend/static')

# 示例数据存储
data_store = {
    "time": datetime.now().strftime("%H:%M:%S"),
    "data": {
        "name": "",
        "gender": "",
        "occupation": "",
        "hobby": ""
    }
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data_store['time'] = datetime.now().strftime("%H:%M:%S")
        data_store['data'] = {
            'name': request.form.get('name'),
            'gender': request.form.get('gender'),
            'occupation': request.form.get('occupation'),
            'hobby': request.form.get('hobbies')
        }
        return redirect(url_for('success'))

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
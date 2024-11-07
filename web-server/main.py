from flask import Flask, request, jsonify

app = Flask(__name__)

# 示例数据存储
data_store = {"message": "Hello from Flask!"}

@app.route('/')
def home():
    return "Welcome to the Flask server!"

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/post_data', methods=['POST'])
def post_data():
    global data_store
    new_data = request.json
    if not new_data:
        return jsonify({"error": "No data provided"}), 400
    data_store.update(new_data)
    return jsonify({"status": "Data updated successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
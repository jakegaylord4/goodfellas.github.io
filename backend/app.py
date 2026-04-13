from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from database.database import get_user, add_user, update_user

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontpage.html')

@app.route('/get_user')
def login():
    email = request.args.get("email")
    password = request.args.get("password")
    user = get_user(email, password)
    if not user:
        return "User not found"
    return "User found"



@app.route('/signup', methods=['POST'])
def add_user_endpoint():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    user = add_user(name, email, password, role)
    return jsonify({"message": "User added", "user": user}), 201

@app.route('/add_user')
def add_user_route():
    return "ADD_USER"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

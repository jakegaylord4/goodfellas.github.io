from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from database.database import get_user, add_user, update_user, update_user_status, get_user_by_id  
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontpage.html')

@app.route('/auth')
def home():
    return render_template('authfrontpage.html')

def get_user_from_email_and_password(email, password):
    return get_user(email, password)



@app.route('/signup', methods=['POST'])
def add_user_endpoint():
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    email = request.form.get("email")
    password = request.form.get("password")


    if not all([firstname, lastname, email, password]):
        return jsonify({"message": "Missing required fields"}), 400
    
    if (email.split("@")[1] != "bowdoin.edu"):
        return jsonify({"message": "Invalid email domain, must be @bowdoin.edu"}), 400
    

    user = add_user(firstname, lastname, email, password)
    
    if not user:
        return jsonify({"message": "Email already in use"}), 409
    user_id = user["id"]
    update_user(user_id, {"status": "active"})
    return jsonify({"message": "User added", "user": user, "user_id": user_id}), 201


@app.route('/login', methods=['POST'])
def login_endpoint():
    email = request.form.get("email")
    password = request.form.get("password")
    if not all([email, password]):
        return jsonify({"message": "Missing email or password"}), 400

    user = get_user_from_email_and_password(email, password)

    if not user:
        return jsonify({"message": "User not found"}), 404

    user_id = user["id"]
    update_user_status(user_id, "active")

    return jsonify({"message": "Login successful", "user": user}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
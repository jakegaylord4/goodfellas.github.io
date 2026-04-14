from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
from database.database import get_user, add_user, update_user, update_user_status, get_user_by_id, get_all_users

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')


@app.route('/')
def home():
    return render_template('frontpage.html')


@app.route('/auth')
def auth():
    if not session.get('user_id'):
        return render_template('frontpage.html')
    return render_template('authfrontpage.html')


@app.route('/me')
def me():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not logged in"}), 401
    user = get_user_by_id(user_id)
    return jsonify({"user": user}), 200


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

    if not email.endswith("@bowdoin.edu"):
        return jsonify({"message": "Invalid email domain, must be @bowdoin.edu"}), 400

    user = add_user(firstname, lastname, email, password)
    if not user:
        return jsonify({"message": "Email already in use"}), 409

    session['user_id'] = user["id"]
    return render_template('authfrontpage.html')


@app.route('/login', methods=['POST'])
def login_endpoint():
    email = request.form.get("email")
    password = request.form.get("password")

    if not all([email, password]):
        return jsonify({"message": "Missing email or password"}), 400

    user = get_user_from_email_and_password(email, password)
    if not user:
        return jsonify({"message": "User not found", "users": get_all_users()}), 404

    session['user_id'] = user["id"]
    update_user_status(user["id"], "active")
    return render_template('authfrontpage.html')


@app.route('/logout', methods=['POST'])
def logout_endpoint():
    user_id = session.get('user_id')
    if user_id:
        update_user_status(user_id, "inactive")
    session.pop('user_id', None)
    return render_template('frontpage.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
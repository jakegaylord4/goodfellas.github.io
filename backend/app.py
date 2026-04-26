from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
import os
from database.database import get_user, add_user, update_user, update_user_status, get_user_by_id

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
        return render_template('frontpage.html', signup_error= "Missing required fields")


    if not email.endswith("@bowdoin.edu"):
        return render_template('frontpage.html', signup_error= "Invalid email domain, must be @bowdoin.edu")

    user = add_user(firstname, lastname, email, password)
    if not user:
        return render_template('frontpage.html', signup_error= "Email already in use")

    session['user_id'] = user["id"]
    return render_template('authfrontpage.html')


@app.route('/login', methods=['POST'])
def login_endpoint():
    email = request.form.get("email")
    password = request.form.get("password")

    if not all([email, password]):
        return render_template('frontpage.html', login_error="Missing email or password")

    user = get_user_from_email_and_password(email, password)
    if not user:
        return render_template('frontpage.html', login_error="User not found. Please check your credentials.")

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

@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/submit_service', methods=['POST'])
def submit_service():
    user_id = session.get('user_id')
    if not user_id:
        return render_template('services.html', error="Not logged in")
    
    service_name = request.form.get("service_name")
    service_description = request.form.get("service_description")
    service_price = request.form.get("service_price")
    service_image = request.form.get("service_image")
    
    if not all([service_name, service_description, service_price, service_image]):
        return render_template('services.html', error="Missing required fields")
    
    add_service(user_id, service_name, service_description, service_price, service_image)
    return render_template('services.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
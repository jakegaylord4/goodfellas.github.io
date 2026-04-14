database = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "password": "password", "status": "active"}
]
id_counter = 2

def get_all_users():
    return database


def add_user(firstname, lastname, email, password):
    global id_counter

    if any(u["email"] == email for u in database):
        return None

    user = {
        "id": id_counter,
        "name": firstname + " " + lastname,
        "email": email,
        "password": password,
        "status": "active"
    }
    id_counter += 1
    database.append(user)
    return user


def get_user(email, password):
    for user in database:
        if user["email"] == email and user["password"] == password:
            return user
    return None


def get_user_by_id(user_id):
    for user in database:
        if user["id"] == user_id:
            return user
    return None


def update_user(user_id, fields: dict):
    for user in database:
        if user["id"] == user_id:
            user.update(fields)
            return True
    return False


def update_user_status(user_id, status):
    return update_user(user_id, {"status": status})


def delete_user(user_id):
    for i, user in enumerate(database):
        if user["id"] == user_id:
            database.pop(i)
            return True
    return False
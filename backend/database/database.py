
database = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "password": "password", "role": "role"}
]
id_counter = 1

def add_user(name, email, password, role):
    global id_counter
    user = {}
    user["id"] = id_counter
    id_counter += 1
    user["name"] = name
    user["email"] = email
    user["password"] = password
    user["role"] = role
    database.append(user)


def get_user(email, password):
    for user in database:
        if user["email"] == email and user["password"] == password:
            return user
    return None


def update_user(user_id, user):
    for i, u in enumerate(database):
        if u["id"] == user_id:
            database[i] = user
            return True
    return False


def delete_user(user_id):
    for i, u in enumerate(database):
        if u["id"] == user_id:
            database.pop(i)
            return True
    return False


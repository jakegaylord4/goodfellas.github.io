user_database = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "password": "password", "status": "active"}
]
id_counter = 2

service_database = [
    {"id": 1, "service_name": "example_service", "service_description": "example_service_description", "service_price": 100, "service_image": "example_service_image"}
]


def add_user(firstname, lastname, email, password):
    global id_counter

    if any(u["email"] == email for u in user_database):
        return None

    user = {
        "id": id_counter,
        "name": firstname + " " + lastname,
        "email": email,
        "password": password,
        "status": "active"
    }
    id_counter += 1
    user_database.append(user)
    return user


def get_user(email, password):
    for user in user_database:
        if user["email"] == email and user["password"] == password:
            return user
    return None


def get_user_by_id(user_id):
    for user in user_database:
        if user["id"] == user_id:
            return user
    return None


def update_user(user_id, fields: dict):
    for user in user_database:
        if user["id"] == user_id:
            user.update(fields)
            return True
    return False


def update_user_status(user_id, status):
    return update_user(user_id, {"status": status})


def delete_user(user_id):
    for i, user in enumerate(user_database):
        if user["id"] == user_id:
            user_database.pop(i)
            return True
    return False

def add_service(user_id,service_name, service_description, service_price, service_image):
    
    
    service = {
        "id": user_id,
        "service_name": service_name,
        "service_description": service_description,
        "service_price": service_price,
        "service_image": service_image
    }
    service_database.append(service)
    return service

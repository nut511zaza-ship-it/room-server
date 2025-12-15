import requests

BASE_URL = "http://127.0.0.1:8000"

def login(username, password):
    r = requests.post(
        f"{BASE_URL}/login",
        json={"username": username, "password": password}
    )
    return r.json()

def register(username, password):
    r = requests.post(
        f"{BASE_URL}/register",
        json={"username": username, "password": password}
    )
    return r.json()

def create_room(username):
    r = requests.post(
        f"{BASE_URL}/create-room",
        params={"username": username}
    )
    return r.json()

def join_room(room_code, username):
    r = requests.post(
        f"{BASE_URL}/join-room",
        params={
            "room_code": room_code,
            "username": username
        }
    )
    return r.json()
def get_room_members(room_code, username):
    r = requests.get(
        f"{BASE_URL}/room-members",
        params={
            "room_code": room_code,
            "username": username
        }
    )
    return r.json()

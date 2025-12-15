import requests

BASE_URL = "https://room-server.onrender.com"

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
        json={"username": username}
    )
    return r.json()


def join_room(username, room_code):
    r = requests.post(
        f"{BASE_URL}/join-room",
        json={
            "username": username,
            "room_code": room_code
        }
    )
    return r.json()

def room_members(username, room_code):
    r = requests.post(
        f"{BASE_URL}/room-members",
        json={
            "username": username,
            "room_code": room_code
        }
    )
    return r.json()


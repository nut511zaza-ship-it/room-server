
from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

rooms = {}  # {room_code: leader_username}

app = FastAPI()

# กล่องเก็บ user (ชั่วคราว)
users = {}

class LoginData(BaseModel):
    username: str
    password: str

# สมัครสมาชิก
@app.post("/register")
def register(data: LoginData):
    if data.username in users:
        return {"success": False, "message": "Username already exists"}

    users[data.username] = data.password
    return {"success": True, "message": "Register success"}

# เข้าสู่ระบบ
@app.post("/login")
def login(data: LoginData):
    if data.username in users and users[data.username] == data.password:
        return {"success": True, "message": "Login success"}

    return {"success": False, "message": "Wrong username or password"}

@app.post("/create-room")
def create_room(username: str):
    # สุ่มรหัสห้อง 6 ตัว
    room_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    rooms[room_code] = {
        "leader": username,
        "members": [username]
    }

    return {
        "room_code": room_code,
        "leader": username
    }
@app.post("/join-room")
def join_room(room_code: str, username: str):
    room_code = room_code.upper()

    if room_code not in rooms:
        return {"success": False, "message": "Room not found"}

    if username in rooms[room_code]["members"]:
        return {"success": True, "room_code": room_code}

    rooms[room_code]["members"].append(username)

    return {
        "success": True,
        "room_code": room_code,
        "leader": rooms[room_code]["leader"]
    }
@app.get("/room-members")
def room_members(room_code: str, username: str):
    room_code = room_code.upper()

    if room_code not in rooms:
        return {"success": False, "message": "Room not found"}

    room = rooms[room_code]

    if room["leader"] != username:
        return {"success": False, "message": "Not leader"}

    return {
        "success": True,
        "members": room["members"]
    }

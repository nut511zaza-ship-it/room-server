from fastapi import FastAPI
from pydantic import BaseModel
import random
import string

app = FastAPI()

users = {}
rooms = {}

# ---------- Models ----------

class LoginData(BaseModel):
    username: str
    password: str

class RoomData(BaseModel):
    username: str
    room_code: str | None = None


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
def create_room(data: RoomData):
    room_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    rooms[room_code] = {
        "leader": data.username,
        "members": [data.username]
    }

    return {
        "success": True,
        "room_code": room_code,
        "leader": data.username
    }

@app.post("/join-room")
def join_room(data: RoomData):
    room_code = data.room_code.upper()

    if room_code not in rooms:
        return {"success": False, "message": "Room not found"}

    if data.username not in rooms[room_code]["members"]:
        rooms[room_code]["members"].append(data.username)

    return {
        "success": True,
        "room_code": room_code,
        "leader": rooms[room_code]["leader"]
    }

@app.post("/room-members")
def room_members(data: RoomData):
    room_code = data.room_code.upper()
    room = rooms.get(room_code)

    if not room:
        return {"success": False, "message": "Room not found"}

    if room["leader"] != data.username:
        return {"success": False, "message": "Not leader"}

    return {"success": True, "members": room["members"]}


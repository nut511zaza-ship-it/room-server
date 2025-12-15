import tkinter as tk
from api import create_room, join_room, get_room_members

class RoomUI:
    def __init__(self, username):
        self.username = username
        self.room_code = None
        self.is_leader = False

        self.root = tk.Tk()
        self.root.title("Room")

        tk.Label(self.root, text=f"User: {username}").pack(pady=5)

        # ===== Create Room =====
        tk.Button(self.root, text="Create Room", command=self.create_room).pack()
        self.room_label = tk.Label(self.root, text="Room Code: -")
        self.room_label.pack(pady=5)

        # ===== Join Room =====
        tk.Label(self.root, text="Join Room Code").pack()
        self.join_entry = tk.Entry(self.root)
        self.join_entry.pack()

        tk.Button(self.root, text="Join Room", command=self.join_room).pack(pady=5)

        # ===== Members =====
        self.member_box = tk.Listbox(self.root, height=6)
        self.member_box.pack(pady=5)

        tk.Button(self.root, text="Refresh Members", command=self.refresh_members).pack()

        self.status = tk.Label(self.root, text="")
        self.status.pack(pady=5)

        self.root.mainloop()

    def create_room(self):
        res = create_room(self.username)
        self.room_code = res["room_code"]
        self.is_leader = True

        self.room_label.config(text=f"Room Code: {self.room_code}")
        self.status.config(text="You are the leader", fg="green")
        self.refresh_members()

    def join_room(self):
        code = self.join_entry.get().strip()
        res = join_room(code, self.username)

        if res.get("success"):
            self.room_code = code.upper()
            self.is_leader = False
            self.room_label.config(text=f"Room Code: {self.room_code}")
            self.status.config(text="Joined room", fg="green")
        else:
            self.status.config(text=res.get("message"), fg="red")

    def refresh_members(self):
        if not self.is_leader or not self.room_code:
            return

        res = get_room_members(self.room_code, self.username)

        if not res.get("success"):
            self.status.config(text=res.get("message"), fg="red")
            return

        self.member_box.delete(0, tk.END)
        for m in res["members"]:
            self.member_box.insert(tk.END, m)

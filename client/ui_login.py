import tkinter as tk
from api import login, register
from ui_room import RoomUI


def on_login():
    user = entry_user.get().strip()
    pwd = entry_pass.get().strip()

    result = login(user, pwd)

    if result.get("success"):
        status.config(text="Login success", fg="green")
        root.destroy()
        RoomUI(user)
    else:
        status.config(text=result.get("message", "Error"), fg="red")


def on_register():
    user = entry_user.get().strip()
    pwd = entry_pass.get().strip()

    result = register(user, pwd)

    if result.get("success"):
        status.config(text="Register success", fg="green")
    else:
        status.config(text=result.get("message", "Error"), fg="red")


# ===== UI =====
root = tk.Tk()
root.title("Login")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=on_login).pack(pady=5)
tk.Button(root, text="Register", command=on_register).pack(pady=5)

status = tk.Label(root, text="")
status.pack()

root.mainloop()

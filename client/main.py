import tkinter as tk
from ui_login import LoginUI
from ui_room import RoomUI

def start_room(username):
    RoomUI(root, username)

root = tk.Tk()
root.title("Group Room System")
root.geometry("300x350")

LoginUI(root, start_room)

root.mainloop()

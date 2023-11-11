from socket import *
import tkinter as tk
import threading
from PIL import ImageTk, Image

class Server:
    def __init__(self):
        self.images = [
            ImageTk.PhotoImage(Image.open("images/1.png")),
            ImageTk.PhotoImage(Image.open("images/2.png")),
            ImageTk.PhotoImage(Image.open("images/3.png")),
            ImageTk.PhotoImage(Image.open("images/4.png")),
        ]
        self.image_index = 0
        self.lab = None

    def change_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        image = self.images[self.image_index]
        self.lab.configure(image=image)
        self.lab.image = image

def start_server(rock_server, server_address):
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(server_address)
    server.listen()

    user, addr = server.accept()

    while True:
        data = user.recv(1)
        if not data:
            break
        rock_server.change_image()

def finish():
    win.destroy()


server_ip = input("Введите IP-адрес сервера: ")
server_port = int(input("Введите порт сервера: "))

server_address = (server_ip, server_port)

win = tk.Tk()
win.title('Rock')
win.geometry("1100x720")
win.config(bg='blue')
win.minsize(256, 256)
img = ImageTk.PhotoImage(Image.open("images/1.png"))
lab = tk.Label(win, image=img)
lab.pack()

rock_server = Server()
rock_server.lab = lab

win.protocol("WM_DELETE_WINDOW", finish)

new_thread = threading.Thread(target=start_server, args=(rock_server, server_address))
new_thread.start()

win.mainloop()
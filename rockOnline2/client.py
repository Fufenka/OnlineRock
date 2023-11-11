import tkinter as tk
from socket import *

class Client:
    def __init__(self, server_address):
        self.win = tk.Tk()
        self.win.title('rock')
        self.win.geometry("300x300")
        self.win.config(bg='red')

        self.btn = tk.Button(self.win, text='ROCK', font="Arial 40", width=5, height=2, command=self.click)
        self.btn.place(relx=0.5, rely=0.5, anchor='center')

        self.server_address = server_address
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(self.server_address)

    def click(self):
        self.client.send(bytes("\00", 'ascii'))

    def finish(self):
        self.client.close()
        self.win.destroy()

    def run(self):
        self.win.mainloop()


server_ip = input("Введите IP-адрес сервера: ")
server_port = int(input("Введите порт сервера: "))


server_address = (server_ip, server_port)


client = Client(server_address)
client.run()
import socket
import threading
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog

<<<<<<< HEAD
HOST = '10.0.0.37'
=======
HOST = '127.0.0.1'
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
PORT = 9999

class Client:
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))
        
        msg = tk.Tk()
        msg.withdraw()
        
        self.nickname = simpledialog.askstring("Nickname","Choose your nickname", parent=msg)
        self.sock.send(self.nickname.encode())
        
        self.gui_done = False
        self.running = True
        
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        
        gui_thread.start()
        receive_thread.start()
    
    def gui_loop(self):
        self.win = tk.Tk()
        self.win.configure(bg="lightgray")
        
        self.chat_label = tk.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.configure(font=("Arial", 12))
        self.chat_label.pack(padx=20,pady=5)        

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20,pady=5)
        self.text_area.config(state='disabled')
        
        self.text_label = tk.Label(self.win, text="Message:", bg="lightgray")
        self.text_label.configure(font=("Arial", 12))
        self.text_label.pack(padx=20,pady=5)
        
        self.input_area = tk.Text(self.win, height=3)
        self.input_area.pack(padx=20,pady=5)
        
        self.send = tk.Button(self.win, text="Send", command=self.write)
        self.send.pack(padx=20,pady=5)
        
        self.gui_done = True
        
        self.text_area.config(state='normal')
        self.text_area.insert('end', "Connected to serveur\n")
        self.text_area.yview('end')
        self.text_area.config(state='disabled')
        
        
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        
        self.win.mainloop()
        
    def stop(self):
        self.running = False
        self.sock.send(f"{self.nickname} has disconected".encode())
        self.win.destroy()
        self.sock.close()
        quit()
        
    def write(self):
        message = f"{self.nickname} : {self.input_area.get('1.0','end')}"
        self.sock.send(message.encode())
        self.input_area.delete('1.0','end')
    
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if self.gui_done:
                    self.text_area.config(state='normal')
                    self.text_area.insert('end', message)
                    self.text_area.yview('end')
                    self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break

client = Client(HOST,PORT)
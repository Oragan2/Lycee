import socket
import customtkinter

class Client:
    def __init__(self):
        HOST = "127.0.0.1"
        PORT = 9999
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST,PORT))
        
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")
        
        self.app = customtkinter.CTk()
        self.app.geometry("400x240")
        self.createGUI()
    
    def createGUI(self):
        self.tabview = customtkinter.CTkTabview(self.app, width=250)
        self.tabview.pack(padx=0,pady=0)
        self.tabview.add("Connexion")
        self.tabview.add("Register")
        
        self.c_user = customtkinter.CTkEntry(self.tabview.tab("Connexion"), placeholder_text="Username")
        self.c_user.pack(padx=20, pady=5)
        
        self.c_mdp = customtkinter.CTkEntry(self.tabview.tab("Connexion"), placeholder_text="Password", show='*')
        self.c_mdp.pack(padx=20, pady=5)
        
        self.c_cb = customtkinter.CTkButton(self.tabview.tab("Connexion"), command=self.conn, text="Connexion")
        self.c_cb.pack(padx=20, pady=5)
        
        self.r_user = customtkinter.CTkEntry(self.tabview.tab("Register"), placeholder_text="Username")
        self.r_user.pack(padx=20, pady=5)
        
        self.r_mdp = customtkinter.CTkEntry(self.tabview.tab("Register"), placeholder_text="Password", show='*')
        self.r_mdp.pack(padx=20, pady=5)
        
        self.r_mdp_verif = customtkinter.CTkEntry(self.tabview.tab("Register"), placeholder_text="Verify your password", show='*')
        self.r_mdp_verif.pack(padx=20, pady=5)
        
        self.r_cb = customtkinter.CTkButton(self.tabview.tab("Register"), command=self.reg, text="Register")
        self.r_cb.pack(padx=20, pady=5)
        
        self.app.mainloop()
    
    def conn(self):
        self.client.send(f"c{self.c_user.get()} : {self.c_mdp.get()}".encode())
        self.c_user.delete(0,'end')
        self.c_mdp.delete(0,'end')
        res = self.client.recv(1024)
        print(res.decode())
    
    def reg(self):
        if self.r_mdp.get() == self.r_mdp_verif.get():
            self.client.send(f"r{self.r_user.get()} : {self.r_mdp.get()}".encode())
            self.r_user.delete(0,'end')
            self.r_mdp.delete(0,'end')
            self.r_mdp_verif.delete(0,'end')
            res = self.client.recv(1024)
            print(res.decode())

Client()
import socket
import sqlite3
import hashlib
import threading

#socket
<<<<<<< HEAD
HOST = "10.0.0.37"
=======
HOST = "0.0.0.0"
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
PORT = 9999

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST,PORT))
serveur.listen(5)

# sqlite3
con = sqlite3.connect("User.db")
cu = con.cursor()
cu.execute("""
           CREATE TABLE IF NOT EXISTS mdp(
               username TEXT PRIMARY KEY NOT NULL,
               password TEXT NOT NULL
           )
           """)
con.commit()

#hashlib
m = hashlib.md5()

def check(user:str,mdp:str):
    global m
    con = sqlite3.connect("User.db")
    cu = con.cursor()
    m.update(user)
    user_d = m.hexdigest()
    m = hashlib.md5()
    m.update(mdp)
    mdp_d = m.hexdigest()
    print(user_d, mdp_d)
    m = hashlib.md5()
    cu.execute("SELECT * FROM mdp WHERE username = ? AND password = ?", (user_d, mdp_d))
    f = cu.fetchall()
    con.close()
    print(type(f), f)
    return f != []

def add(user:str,mdp:str):
    global m
    con = sqlite3.connect("User.db")
    cu = con.cursor()
    m.update(user)
    user_d = m.hexdigest()
    m = hashlib.md5()
    m.update(mdp)
    mdp_d = m.hexdigest()
    m = hashlib.md5()
    print(user_d,mdp_d)
    try:
        cu.execute("INSERT INTO mdp VALUES (?,?)", (user_d,mdp_d))
        con.commit()
        con.close()
        print("test")
        return "Worked"
    except:
        return "Didn't work"

def handle(client:socket, mode:bool, info:bytes):
    user = info[:info.rfind(b':')-1]
    mdp = info[info.rfind(b':')+2:]
    print(user, mdp)
    if mode:
        if check(user,mdp):
            client.send("Info correct".encode())
<<<<<<< HEAD
        else:
            client.send("Info incorrect".encode())
=======
            client.close()
        else:
            client.send("Info incorrect".encode())
            client.close()
>>>>>>> fc9acc5024275baf41e857549168f97a380f1a0b
    else:
        resp = add(user,mdp)
        client.send(resp.encode())
        client.close()

def receive():
    while True:
        client, addr = serveur.accept()
        print(f"Connected to {addr}")
        info = client.recv(1024)
        d = info.decode()[0]
        if d == 'c':
            hand = threading.Thread(target=handle, args=(client,True,info[1:]))
        else:
            hand = threading.Thread(target=handle, args=(client,False,info[1:]))
        hand.start()

print("Serveur running")
receive()
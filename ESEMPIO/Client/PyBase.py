import socket


class PyBase():
    HOST = "127.0.0.1"
    PORT = 9999

    Username = ""
    Password = ""
    
    def connect(self, host, port, username, password, group, var, action):
        self.HOST = host
        self.PORT = port
        self.Username = username
        self.Password = password

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((host,port))
        info = {"info":{"user":username,"pass":password},"cmd":{"group":group,"var":var,"action":action}}
        s.send(str(info).encode())

        return s.recv(1024).decode()
        


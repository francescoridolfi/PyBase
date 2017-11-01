import socket
import threading
import ast
from random import randint


class ThreadedServer(object):
    Username = "root"
    Password = "pippo"
    auths = [] 
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("Listening...")
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    info = ast.literal_eval(data.decode())
                    user = info["info"]["user"]
                    passwd = info["info"]["pass"]
                    if(user == self.Username and passwd == self.Password):
                        print("Authorized: "+str(address))
                        cmd = info["cmd"]
                        group = cmd["group"]
                        var = cmd["var"]
                        action = cmd["action"]
                        if(action[:3] == "SET"):
                            if(action[4:] != ""):
                                try:
                                    file = open(group,"r")
                                    read = file.read()
                                    file.close()
                                    variables = ast.literal_eval(read)
                                    variables[var] = action[4:]
                                    file = open(group,"w")
                                    file.write(str(variables))
                                    file.close()
                                except:
                                    variables = {var:action[4:]}
                                    file = open(group,"w")
                                    file.write(str(variables))
                                    file.close()
                                data = "I have write '"+action[4:]+"' in '"+var+"' variable in '"+group+"' group!"
                                client.send(data.encode())
                            else:
                                data = "The value can't be null!"
                                client.send(data.encode())
                        elif(action == "GETALL"):
                            try:
                                file = open(group,"r")
                                read = file.read()
                                file.close()
                                client.send(read.encode())
                            except:
                                data = "ERROR: The group is not existent!"
                                client.send(data.encode())
                        elif(action == "GET"):
                            try:
                                file = open(group,"r")
                                read = file.read()
                                file.close()
                                variables = ast.literal_eval(read)
                                data = variables[var]
                                client.send(str(data).encode())
                            except:
                                data = "ERROR: The group or variable is not existent!"
                                client.send(data.encode())
                        elif(action == "DEL"):
                            try:
                                file = open(group,"r")
                                read = file.read()
                                file.close()
                                variables = ast.literal_eval(read)
                                del variables[var]
                                file = open(group,"w")
                                file.write(str(variables))
                                file.close()
                                data = "The variable was deleted!"
                                client.send(str(data).encode())
                            except:
                                data = "ERROR: The group or variable is not existent!"
                                client.send(data.encode())
                    else:
                        data = "ERROR: The username or password are incorrects!"
                        client.send(data.encode())
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()

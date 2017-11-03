import PyBase
import ast

#== DATABASE ==#
PyBase = PyBase.PyBase()

host = '127.0.0.1'
port = 8888

user = "root"
passwd = "pippo"

def execute(cmd):
    result = PyBase.connect(host,port,user,passwd,cmd["group"],cmd["var"],cmd["action"])
    return result

#== DATABASE ==#

username = input("Put here your username! ")

while True:
    Chat = execute({"group":"chat","var":"","action":"GETALL"})
    if(Chat == "ERROR: The group is not existent!"):
        execute({"group":"chat","var":"Server","action":"SET Welcome to the chat!"})
        Chat = execute({"group":"chat","var":"","action":"GETALL"})
    Chat = ast.literal_eval(Chat)
    
    for k in Chat:
        print("%s >> %s" % (k,Chat[k]))
    msg = input("> ")
    execute({"group":"chat","var":username,"action":"SET "+str(msg)})



"""
cmd = {"group":"test","var":"ridolfinotv","action":"SET stupendo"}
execute(cmd)

cmd = {"group":"test","var":"","action":"GETALL"}
result = execute(cmd)

print(result)
"""

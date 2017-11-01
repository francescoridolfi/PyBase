import PyBase

PyBase = PyBase.PyBase()

host = '127.0.0.1'
port = 9999

user = "root"
passwd = "pippo"

def execute(cmd):
    result = PyBase.connect(host,port,user,passwd,cmd["group"],cmd["var"],cmd["action"])
    return result

cmd = {"group":"test","var":"ridolfinotv","action":"SET stupendo"}
execute(cmd)

cmd = {"group":"test","var":"","action":"GETALL"}
result = execute(cmd)

print(result)

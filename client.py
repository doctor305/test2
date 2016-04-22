import socket

target_host = "127.0.0.1"
target_port = 9999
buf = ""

def get_file(string):
    try:
        ls = string.split()
        com = ls[0]
        sourse = ls[1]
        target = ls[2]
    except:
        com = ""
        sourse = ""
        target = ""
    return com,sourse,target
        

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
print "[*] Connect to "+ target_host + ": " + str(target_port)

print "[*] For example: \n[*] send C:\\a.zip C:\\a.zip \n[*] recv C:\\a.zip c:\\b.zip\n"
command = raw_input("[*] Input the command: ")
print "[*] Wait ..."

com,sourse,target = get_file(command)
if com =="send":
    client.send(command)
    f = open(sourse,"rb")
    while True:
        data = f.read(2048)
        if data == "":
            break
        client.send(data)
    f.close()
    client.send("complete!")
    print "[*] Send complete!" 
elif com =="recv":
    client.send(command)
    f = open(target,"wb")
    while True:
        data = client.recv(4096)
        if data != "complete!":
            f.write(data)
        else:
            break
    f.close()
    print "[*] complete!\n"
else:
    print "[*] wrong command\n"

client.close()

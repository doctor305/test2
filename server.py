import socket
import threading
import time

bind_ip   = "127.0.0.1"
bind_port = 9999

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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

def handle_client(client_socket):
    request = client_socket.recv(2048)
    com, sourse, target = get_file(request)
    if com == "send":
        print "[*] Received: %s" % request
        f = open(target,"wb")
        while True:
            data = client_socket.recv(2048)
            if data != "complete!":
                f.write(data)
            else:
                break
        f.close()
        print "[*] Recever complete!\n"
    elif com == "recv":
        print "[*] Received: %s" % request
        f = open(sourse,"rb")
        while True:
            data = f.read(2048)
            if data == '':
                break
            client_socket.send(data)
        f.close()
        client_socket.send("complete!")
        print "[*] Send complete!\n"
    else:
        client_socket.send("ERROR!")
##    client_socket.send(res)
##    print client_socket.getpeername()
    client_socket.close()


while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()



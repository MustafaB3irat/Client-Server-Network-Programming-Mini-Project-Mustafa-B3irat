import socket
import os


def listFiles(client):
    files =""
    for entry in os.scandir('.'):
        if entry.is_file() and entry.name.endswith(".txt"):
            files += entry.name +" \n"
    return client.sendall(files.encode('utf-8'))

def retrieveFile(filename , client):
    if os.path.isfile(filename) and filename.endswith(".txt"):
        with open(filename , "r") as f:
                bytes = f.read()

                if not bytes:
                    f.close()
                    return client.sendall("This file is Empty!\n".encode('utf-8'))

                else:
                    f.close()
                    return client.sendall(bytes.encode('utf-8'))
    else:
        return client.send("No such File! \n".encode('utf-8'))



if(__name__ == '__main__'):
    server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(socket.gethostname())
    port = 8888
    address = (ip,port)
    server.bind(address)
    server.listen(1)
    print ("[*] started listining on ",ip," on port ",port)
    while True:
        client,addr=server.accept()
        print ("[*] Got a connection from ",addr[0]," : ",addr[1])

        data = client.recv(1024).decode('utf-8')
        print ("[*] Recieved Data...")
        if(data == '1'):
            listFiles(client)

        elif(data == '3'):
            print ("[*] closing connection...")
            client.close()
            server.close()
            exit()
        else:
            retrieveFile(data , client)


        print ("[*] closing connection...")
        client.close()

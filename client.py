import socket

if(__name__ == '__main__'):
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = socket.gethostbyname(socket.gethostname())
        port = 8888
        address= (ip , port)
        client.connect(address)
        inp=input("\n\n[*] 1. list server's files \n[*] 2. Enter File name to show content.\n[*] 3. Quit\n")
        if(inp == '1' or inp == 'ls'):

            client.sendall(inp.encode('utf-8'))
            data= client.recv(1024)
            while True:
                if not (data):
                    break

                print (data.decode('utf-8'))
                data= client.recv(1024)

            print ("\n Done \n")

        elif(inp == '2'):
            file = input("\n [*] Please Enter File name from the list! \n")
            client.sendall(file.encode('utf-8'))

            data = client.recv(1024).decode('utf-8')

            if data != "No such File! \n":
                print ("\nFile content: \n\n [*]  " + data)

            while True:
                if not (data):
                    break
                print (data)
                data = client.recv(1024).decode('utf-8')

            print ("\n[*]\n")
        elif(inp == '3'):
            client.send(inp.encode('utf-8'))
            print ("\n[*] closing connection...\n")
            client.close()
            exit()

        else:
            print ("[*] Please Choose 1 or 2 ...")

        client.close()

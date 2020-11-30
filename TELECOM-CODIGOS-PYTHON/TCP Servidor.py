import socket

host="localhost"
port=5656

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))
server.listen(1)

print("servidor en espera")

active, addr= server.accept()

while True:

    recibido=active.recv(1024)

    print("cliente", recibido.decode(encoding="ascii", errors="ignore"))

    enviar= input("server")

    active.send(enviar.encode(encoding="ascii", errors="ignore"))

    active.close()
    

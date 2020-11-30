import socket

host ="localhost"
port =5656

objsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
objsocket.connect((host,port))

print("iniciamos llamada")

while True:
    enviar= input("cliente")
    objsocket.send(enviar.encode(encoding="ascii", errors="ignore"))

    recibido= objsocket.recv(1024)

    print(" servidor", recibido.decode(encoding="ascii", errors="ignore"))

    objsocket.close()

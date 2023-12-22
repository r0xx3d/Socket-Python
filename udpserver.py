import socket

IP = '172.25.209.47'
PORT = 9998
buffersize = 1024

msgFromServer = "hello rohit"
bytesToSend = str.encode(msgFromServer)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((IP,PORT))
print('Listening')

while True:
    bytesAddressPair = server.recvfrom(buffersize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = f"Message from Client:{message}"

    print(clientMsg)

    server.sendto(bytesToSend,address)
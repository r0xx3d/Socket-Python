import socket

target_ip = '172.25.209.47'
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b'hello friend',(target_ip,target_port))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()



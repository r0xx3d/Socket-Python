import socket


target_host = '172.25.209.47'
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"hello devesh")

response = client.recv(4096)

print(response.decode())
client.close()


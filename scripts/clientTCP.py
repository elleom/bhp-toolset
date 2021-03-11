import socket

target_host = "www.google.com"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((target_host, target_port))

# send (P3 encoded)
client.send("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n".encode())
# receive
response = client.recv(4096)

print(response)
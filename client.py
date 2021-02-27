import socket
import sys

server_ip = sys.argv[1]
server_port = sys.argv[2]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    address = input()
    s.sendto(bytes(str(address), "utf-8"), (str(server_ip), int(server_port)))
    data, addr = s.recvfrom(1024)
    print(str(data.decode("utf-8").split(",")[1]))

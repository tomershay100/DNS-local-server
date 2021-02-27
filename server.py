import socket
import sys
import time

my_port = int(str(sys.argv[1]))
ip_father = str(sys.argv[2])
port_father = int(sys.argv[3])
ips_file_name = str(sys.argv[4])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', my_port))

ips_file = open(ips_file_name, "r+")
while True:
    ips_file.close()
    ips_file = open(ips_file_name, "r+")
    count = 0
    data, addr = s.recvfrom(1024)
    for line in ips_file:
        line_arr = line.split(",")
        if line_arr[0] == data.decode("utf-8"):
            if len(line_arr) > 3:
                if float(time.time()) - float(line_arr[3]) > float(line_arr[2]):
                    with open(ips_file_name, "r") as f:
                        lines = f.readlines()
                    with open(ips_file_name, "w") as f:
                        counter = 0
                        for line2 in lines:
                            if line2.strip("\n") != line:
                                if counter == 0:
                                    f.write(line2[:-1])
                                else:
                                    f.write("\n" + line2[:-1])
                                counter += 1
                    break
            temp_str = line_arr[0] + "," + line_arr[1] + "," + line_arr[2]
            s.sendto(bytes(temp_str, "utf-8"), addr)
            count += 1
            break
    if count == 0:  # didnt find the address
        if port_father == -1:
            break
        s_parent = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s_parent.sendto(bytes(data.decode("utf-8"), "utf-8"), (ip_father, port_father))
        data_from_father, addr_from_father = s_parent.recvfrom(1024)
        s.sendto(data_from_father, addr)
        ips_file.write("\n" + data_from_father.decode("utf-8") + "," + str(time.time()))

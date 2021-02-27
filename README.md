# DNS-local-server
\[Assignment in the course ```Introduction to Communication Networks```\]
1. [Introduction](#introduction)
2. [Dependencies](#dependencies)  
3. [Installation](#installation)


## Introduction
Python implementation for DNS server and client. The server holds a ```.txt``` file that contains mapping addresses and IP & port addresses of a higher DNS server. When a client requests a domain, the server will look in its .txt file for the appropriate IP address and return it to the client. If the server is not found, it will contact its "father" (the DNS server above it) requesting the IP address of that domain. Then, when it gets the answer, the server will keep it for TTL time in its mapping file. In this implementation there is an assumption that there is some server in the hierarchy that knows the requested domain.

## Dependencies
* Windows / Linux / macOS with python3
* Git

## Installation
1. Clone the repository:  
    ```
    $ git clone https://github.com/tomershay100/DNS-local-server.git
    ```
2. Run the server using python3:
    ```
    $ python3 server.py 12345 127.0.0.1 11223 ips.txt
    ```
    With "12345" as the server's port number (you can choose a free port as you like), "127.0.0.1" and "11223" as the IP and port addresses of the higher DNS server and "ips.txt" as a ```.txt``` mapping file. In order to run a root server (without a server above it) you must put -1 in the DNS server addresses as follows: ```$ python3 server.py 12345 -1 -1 ips.txt```.
3.  Run the client using python3. The client will receive as arguments the IP and port of the DNS server as follows:
    ```
    $ python3 client.py 127.0.0.1 12345
    ```
    With "12345" as the server's port number (you can choose a free port as you like) and "127.0.0.1" as the server's IP.
4. Enter the required domain as input next to the customer. For example, for "mail.google.com" the output will be 9.9.9.9 (as long as it is written in an ips.txt file).


You can run the client and the DNS servers on the same computer (different terminal) or on another computer on the same network.

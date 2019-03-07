import time
import socket
from File import test_file

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = test_file
    addr = ("127.0.0.1", 12000)

    start = time.time()
    client_socket.sendto(message, addr)

    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print("ping to " + addr[0] + ', ' + "seq = " + str(pings) + ", " + "rtt = " + str(elapsed) + "ms")
    except socket.timeout:
        print('REQUEST TIMED OUT')
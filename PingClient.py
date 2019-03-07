import time
import socket

time_rec = []

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = "TEST MSG"
    addr = ("127.0.0.1", 12000)

    start = time.time()
    client_socket.sendto(message, addr)

    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        time_rec.append(elapsed)
        print("ping to " + addr[0] + ', ' + "seq = " + str(pings) + ", " + "rtt = " + str(elapsed) + "ms")

    except socket.timeout:
        print("ping to " + addr[0] + ', ' + "seq = " + str(pings) + ", " + "rtt = " + 'PACKET LOST')

print("\nmax time = {} \nmin time = {} \navg time = {}\n".format(max(time_rec), min(time_rec), sum(time_rec)/len(time_rec)))

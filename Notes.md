## multiThreading

```python
import threading

t1 = threading.Thread(target=function1, args=(argument tupple))
t2 = threading.Thread(target=function2, args=(argument tupple))


t1.start()
t2.start() 

t1.join() # join the pool and excute simutanously
t2.join() # will wait untill two threads done

threading.Lock(): within a lock, only one thread can run at a time
semaphore: allow more than one lock 
```

## Socket:

```python
# takes a tuple of the address and port
connet((hostname,port))
```

# TCP
## TCP server:

```python
import socket
def Main():
    host = ''
    port = int > 1024 (reserve space)

    # create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to the port
    s.bind((host,port))
    # accept 1 connection at a time
    s.listen(1)
    # store the connection socket that accpet and the source address
    c, addr = s.accept() # return new socket
    pirnt("connection from: " + str(addr))

    while True:
        # receiving 1024 bytes at a time and decode back to a str
        data = c.recv(1024).decode('utf-8')
        # if no more data, break the loop
        if not data:
            break
        print("From connected user: " + data)
        # encode to binary
        c.send(data.encode'utf-8')
    # close connection
    c.close()
    
if __name__ == '__main__':
    Main()
```

## TCP client:

```python   
import socket

def Main():
    host = ''
    port = int > 1024 (reserve space)

    s = socket.socket()
    s.connect((host,port))
    
    message = input("->")
    # while input is not "quit"
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('Recieved from server: ' + data)
        # re-ask for msg
        message = input("->")
    # close connection
    s.close()

if __name__=='__main__':
    Main()
```

# UDP
## UDP server

```python
import socket

def Main():
    host = ''
    port = int > 1024

    # 1st arg: tuple of host and port
    # 2nd arg: "data gram", UDP
    s = socket.socket((socket.AF_INET, socket.SOCK_DGRAM)) 
    s.bind((host,port))

    print("Server Started")
    while True:
        # connectionless, need to store received data and addr
        data, addr = s.recvform(1024)
        data = data.decode('utf-8')
        print('msg form: ' + str(addr))
        print('form connected user: ' + data)
        print("sending: " + data)
        # send data to received addr
        s.sendto(data.encode("utf-8"), addr)
    s.close()

if __name__ == '__main__':
    Main()
```

## UDP client

```python
import socket

def Main():
    host = ''
    port = int > 1024 # diff from server

    server = (host, serverPort)
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind the socket to the client port
    s.bind((host,port))

    message = input("->")
    while message != 'q':
        # encode msg and send to server(tuple)
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('received form server: ' + data)
        message = input("->")
    s.close()

if __name__ == '__main__':
    Main
    

```
import time
import random
import socket
import threading
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

FILE_REQUEST = 2
FILE_RESPONSE = 1
QUIT_NOTIFY = 3
INVALID = -1
FINISH = False

print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
myId = int(sys.argv[1])
mySucc1 = int(sys.argv[2])
mySucc2 = int(sys.argv[3])
myPrev1 = None
myPrev2 = None
dropRate = float(sys.argv[5])

assert(type(myId) is int and myId >= 0 and myId <= 255)
assert(type(mySucc1) is int and mySucc1 >= 0 and mySucc1 <= 255)
assert(type(mySucc2) is int and mySucc2 >= 0 and mySucc2 <= 255)
assert(dropRate >= 0 and dropRate <= 1)

print('set up peer with id ' + sys.argv[1])

# print("PL is alive: " + str(UDPL.is_alive()))
# print("pS is alive: " + str(UDPS.is_alive()))
# print("tH is alive: " + str(TCPH.is_alive()))


'''
print("Enumerate: ")
for e in threading.enumerate():
    print(e)
'''
def validateFileName(str):
    try:
        file = str.split()[1]
    except IndexError:
        raise ValueError('No file name input')
    else:
        if len(file) != 4:
            raise ValueError('File name msut be 4 digits')
        else:
            try:
                file = int(file)
            except:
                raise ValueError('File name must be integer')
            else:
                if (file < 0 or file > 9999):
                    raise ValueError(
                        'File name must be between 0 and 9999')
                return file

def checkFile(file):
    global myId, myPrev1, myPrev2
    
    assert(type(file) is int and file >= 0 and file <= 9999)
    expectedPeer = hashFunc(file)
    assert(type(expectedPeer) is int)
    
    if myId == expectedPeer:
        return True
    
    elif myId > myPrev1 or myId > myPrev2:
        if (myId >= expectedPeer) and ((myPrev1 < expectedPeer) or (myPrev2 < expectedPeer)):
            return True
        else:
            return False

    # if I'm the first peer in the dht
    elif myId < myPrev1 and myId < myPrev2:
        if myId >= expectedPeer:
            return True
        else: 
            return False

def hashFunc(file):
    assert(type(file) is int and file >= 0 and file <= 9999)
    hash = file % 256
    return hash

def extractHeader(protocol, msg):
    msg = msg.split()
    headerSize = 3

    header = msg[0:headerSize]
    msg = ' '.join(msg[headerSize:])
    return (header, msg)

def generateHeader(protocol, flag=None):
    global myId, mySucc1, mySucc2, myPrev1, myPrev2
    
    baseHeader = f'{myId} {myId+50000}'

    if protocol == 'TCP':
        assert(flag is not None)
        TCPheader = f'{baseHeader} {flag}'
        check = TCPheader.split()
        assert(len(check) == 3)
        return TCPheader

    elif protocol == 'UDP':
        return baseHeader

def updatePrev(srcId, srcPos):
    global myPrev1, myPrev2
    
    assert(type(srcId) is int)
    if srcPos == 'Prev1':
        myPrev1 = srcId
    elif srcPos == 'Prev2':
        myPrev2 = srcId
    else:
        print("fail to update prev")
                
def updateNext(new_Succ1, new_Succ2):
    global mySucc1, mySucc2
    
    if new_Succ1 is None:
        assert(type(new_Succ2) is int)
        mySucc2 = new_Succ2
        
    elif new_Succ2 is None:
        assert(type(new_Succ1) is int)
        mySucc1 = new_Succ1
        
    else:
        mySucc1 = new_Succ1
        mySucc2 = new_Succ2
    print(f"My first successor is now peer {mySucc1}.")
    print(f"My second successor is now peer {mySucc2}.")

def notifyDepart(id):
    print(f'Peer {id} will depart from the network.')


def sendTCPMsg(msg, destPort):
    destPort = int(destPort)
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect(('localhost', destPort))
    send_socket.send(msg.encode('utf-8'))
    send_socket.close()


'''
Threading function
'''
def inputMonitor():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH

    while(True):
        if FINISH:
            print("inputMonitor exiting...")
            break
        
        s = input()
        print("get input " + s)
        try:
            flag = s.split()[0]
            print(f"flag is: {flag}")
        except:
            print('invalid')
            continue
        else:
            if flag == 'request':
                try:
                    file = validateFileName(s)
                except ValueError as er:
                    print(er)
                    continue
                else:
                    print(f'successfully validate file {file}')
                    selfPort = 50000+int(myId)
                    print(f'preparing to send to {selfPort}')
                    TCPheader = generateHeader('TCP',FILE_REQUEST)
                    msg = TCPheader + f' {file}'
                    print(f'msg: {msg}')
                    sendTCPMsg(msg, selfPort)
                    print(f'successfully send to port {selfPort}')

            elif flag == 'quit':
                    TCPheader = generateHeader('TCP',QUIT_NOTIFY)
                    mySuccessors = f'{mySucc1} {mySucc2}'
                    prev_port = 50000+myPrev1
                    secPrev_port = 50000+myPrev2

                    msg = f'{TCPheader} {mySuccessors} Peer {myId} will depart from the network.'
                    sendTCPMsg(msg, prev_port)
                    sendTCPMsg(msg, secPrev_port)
                    FINISH = True
                    sys.exit()
            else:
                print('try again')

def UDPSender():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH

    print("UDP Sender thread: start sending ping")
    logging.debug('running with %s', myId)
    while True:
        if FINISH:
            print("UDPSender exiting...")
            break
        sendMsg = "A ping request message was received from Peer " + \
            str(myId)
        c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        UDPheader = generateHeader('UDP')
        for s in [mySucc1, mySucc2]:
            if s is mySucc1:
                myPos = 'Prev1'
            elif s is mySucc2:
                myPos = 'Prev2'
            else: 
                raise Exception
            sendMsg = f'{UDPheader} {myPos} [UDP client {s}] A ping request was received from Peer {myId}.'
            rand = random.randint(0, 10)
            if rand >= dropRate:
                server = ('localhost', (50000+s))
                c_socket.sendto(sendMsg.encode('utf-8'), server)
            c_socket.settimeout(3.0)
            try:
                data, serverAddr = c_socket.recvfrom(1024)
            except socket.timeout:
                print(f"Sender thread: <PACKET LOST> to Peer {s}")
            else:
                print(f"Sender thread: {data.decode('utf-8')}")
        c_socket.close()
        time.sleep(30)

def UDPListener():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH

    print('UDP Listener thread: UDP server with id ' + str(myId) + ' started')
    logging.debug('running with %s', myId)
    
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = 'localhost'
    port = 50000 + myId
    server = (host, port)
    # bind a socket for UDP listener
    s_socket.bind(server)

    
    while True:
        if FINISH:
            print("UDPListener exiting...")
            break
        
        recvMsg, srcAddr = s_socket.recvfrom(1024)
        recvMsg = recvMsg.decode('utf-8')
        header, msg = extractHeader('UDP', recvMsg)
        srcId = int(header[0])
        # srcPort = int(recvMsg[1])
        # srcAddr = ('localhost', srcPort)
        print('Listener thread: [UDP server ' +
                str(myId) + ']' + 'received msg: ' + msg)
        if "response" in recvMsg:
            pass
        elif "request" in recvMsg:
            srcPos = header[2]
            print(f'Listener thread: received from Peer {srcId}, which is my {srcPos}')
            updatePrev(srcId, srcPos)
            print(f"Peer {myId}: [Prev: {myPrev1}] [nextPrev: {myPrev2}]")
            sendMsg = f"A ping response message was received from Peer {myId}."
            s_socket.sendto(sendMsg.encode('utf-8'), srcAddr)

def TCPHandler():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2,FINISH

    print(f'TCP handler thread with id {myId}: Start listening')
    logging.debug('running with %s', myId)

    # create socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('localhost', 50000+myId))

    while(True):
        if FINISH:
            print("TCPHandler exiting...")
            listen_socket.close()
            break
        listen_socket.listen(1)
        # connection socket
        conn, addr = listen_socket.accept()
        print(
            f'TCP handler thread widh id {myId}: Connection from {addr}')
        # receive data from connection socket
        data = conn.recv(1024).decode('utf-8')
        print(f'TCP handler thread with id {myId}: received "{data}"')
        header, recvMsg = extractHeader("TCP", data)
        print(f'TCP handler received data: {data}')
        print(f'TCP handler received header: {header}')
        print(f'TCP handler received recvMsg: {recvMsg}')
        msgType = int(header[2])
        # sending/forwarding reqeust for file
        if msgType is FILE_REQUEST:
            file = int(recvMsg.split()[0])
            # extract file name
            has = checkFile(file)
            print(f"Lookingfor file {file}")
            # if self has the file, connect and send response directly to requesting peer
            if has:
                requestingPeer = header[0]
                requestingPort = header[1]
                TCPheader = generateHeader('TCP', FILE_RESPONSE)
                msg = f'{TCPheader} {file}'
                sendTCPMsg(msg, requestingPort)
                print(
                    f"TCP handler: File {file} is stored here.\nA response message, destined for peer {requestingPeer}, has been sent.")

            # if self doesn't has file, connect and send request next peer
            elif not has:
                print(f"TCP handler: File {file} is not stored here.")
                nextPort = mySucc1 + 50000
                msg = ' '.join(header) + f' {file}'
                sendTCPMsg(msg, nextPort)
                print(
                    "TCP handler: File request message has been forwarded to my successor.")

        # when the file holder send back response to requesting peer
        elif msgType is FILE_RESPONSE:
            file = int(recvMsg.split()[0])
            respondingPeer = header[0]
            print(
                f"TCP handler: Received a response message from peer {respondingPeer}, which has the file {file}.")

        # when the peer is leaving
        elif msgType is QUIT_NOTIFY:
            recvMsg = recvMsg.split()
            leavingPeer = int(header[0])
            assert(len(recvMsg) > 2)
            
            if leavingPeer == mySucc1:
                new_Succ1 = int(recvMsg[0])
                new_Succ2 = int(recvMsg[1])
                
            elif leavingPeer == mySucc2:
                new_Succ1 = None
                new_Succ2 = int(recvMsg[0])
                
            print(f"My new Succ1 should be: {new_Succ1}, new Succ2 should be: {new_Succ2}")    
            updateNext(new_Succ1, new_Succ2)
            
            depart_msg = ' '.join(recvMsg[2:])
            print(depart_msg)
            

        conn.close()

# initialise threads
# tInputMonitor = threading.Thread(target=inputMonitor)
tUDPSender = threading.Thread(target=UDPSender)
tUDPListener = threading.Thread(target=UDPListener)
tTCPHandeler = threading.Thread(target=TCPHandler)

# start all threads
# tInputMonitor.start()
tUDPSender.start()
tUDPListener.start()
tTCPHandeler.start()

while(True):
        if FINISH:
            print("inputMonitor exiting...")
            break

        s = input()
        print("get input " + s)
        try:
            flag = s.split()[0]
            print(f"flag is: {flag}")
        except:
            print('invalid')
            continue
        else:
            if flag == 'request':
                try:
                    file = validateFileName(s)
                except ValueError as er:
                    print(er)
                    continue
                else:
                    print(f'successfully validate file {file}')
                    selfPort = 50000+int(myId)
                    print(f'preparing to send to {selfPort}')
                    TCPheader = generateHeader('TCP', FILE_REQUEST)
                    msg = TCPheader + f' {file}'
                    print(f'msg: {msg}')
                    sendTCPMsg(msg, selfPort)
                    print(f'successfully send to port {selfPort}')

            elif flag == 'quit':
                    TCPheader = generateHeader('TCP', QUIT_NOTIFY)
                    mySuccessors = f'{mySucc1} {mySucc2}'
                    prev_port = 50000+myPrev1
                    secPrev_port = 50000+myPrev2

                    msg = f'{TCPheader} {mySuccessors} Peer {myId} will depart from the network.'
                    sendTCPMsg(msg, prev_port)
                    sendTCPMsg(msg, secPrev_port)
                    FINISH = True
                    sys.exit()
            else:
                print('try again')
print("thread killed")
import time
import random
import socket
import pickle, itertools
import threading
import sys
import logging
import time
import copy

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

FILE_REQUEST = 2        # requesting a file
FILE_RESPONSE = 1       # responding to requesting peer that I have the file
QUIT_NOTIFY = 3         # notifying others that I'm leaving
INFO_REQUEST = 4        # requesting my successors infomation
INFO_RESPONSE = 5       # response to INFO_REQUEST
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
class PingMsg:
    #newSeq = itertools.count()

    def __init__(self, seq, id, flag, myPos):
        #self._seq = next(self.newSeq)
        self._seq = seq
        self._id = id
        self._flag = flag
        self._myPos = myPos

    @property
    def seq(self):
        return self._seq

    @property
    def id(self):
        return self._id

    @property
    def flag(self):
        return self._flag

    @property
    def myPos(self):
        return self._myPos

    @property
    def msg(self):
        if (self.flag == 'REQUEST'):
            msg = f"A ping request was received from Peer {self._id}."
        elif (self.flag == 'RESPONSE'):
            msg = f"A ping response message was received from Peer {self._id}."
        else:
            msg = None
        return msg

    @flag.setter
    def flag(self, flag):
        self._flag = flag

    @myPos.setter
    def myPos(self, pos):
        self._myPos = pos

    @id.setter
    def id(self,id):
        self._id = id

    def __str__(self):
        header = f'{self._seq} {self._id} {self._id+50000} {self._flag} {self._myPos}'
        send_msg = f'header: {header}, msg: {self.msg}'
        return send_msg

class TCPMsg:

    def __init__(self, id, flag, myPos, msg):
        self._id = id
        self._flag = flag
        self._myPos = myPos
        self._msg = msg

    @property
    def id(self):
        return self._id

    @property
    def flag(self):
        return self._flag

    @property
    def myPos(self):
        return self._myPos

    @property
    def msg(self):
        return self._msg

    @flag.setter
    def flag(self, flag):
        self._flag = flag

    @myPos.setter
    def myPos(self, pos):
        self._myPos = pos

    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        header = f'{self._id} {self._id+50000} {self._flag} {self._myPos}'
        send_msg = f'{header} {self.msg}'
        return send_msg

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
                    raise ValueError('File name must be between 0 and 9999')
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
        if myId >= expectedPeer or (expectedPeer > myPrev1) :
            return True
        else:
            return False

def hashFunc(file):
    assert(type(file) is int and file >= 0 and file <= 9999)
    hash = file % 256
    return hash

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

def sendTCPMsg(msg, destId):
    destId = int(destId)
    destPort = 50000 + destId
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        send_socket.connect(('localhost', destPort))
        send_socket.send(msg)
    except:
        time.sleep(1)
        send_socket.connect(('localhost', destPort))
        send_socket.send(msg)
    send_socket.close()

def sendUDPMsg(msg, destId):
    global myId, mySucc1, mySucc2, myPrev1, myPrev2

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rand = random.randint(0, 10)
    if rand >= dropRate:
        destPort = 50000 + destId
        destServer = ('localhost', destPort)
        c_socket.sendto(msg, destServer)
    else:
        print(f"---------<<PACKET LOST>> dest to {destId}----------\n")
    c_socket.close()

'''
Threading function
'''

def pingSender():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH
    print("UDP Sender thread: start sending ping")
    logging.debug('running with %s', myId)
    seqNum = 0

    while not FINISH:
        for s in [mySucc1, mySucc2]:
            if s is mySucc1:
                myPos = 'Prev1'
            elif s is mySucc2:
                myPos = 'Prev2'
            else:
                raise Exception

            sendPing = PingMsg(seqNum, myId, 'REQUEST', myPos)
            send_data = pickle.dumps(sendPing)
            sendUDPMsg(send_data, s)
            print(f'------------Sending Ping to Peer {s}------------\n')

        seqNum += 1
        time.sleep(10)
    

    print("pingSender exiting...")

def UDPListener():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH
    lastPing = {'Succ1': 0, 'Succ2': 0}
    print('UDP Listener thread: UDP server with id ' + str(myId) + ' started')
    logging.debug('running with %s', myId)

    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = 'localhost'
    port = 50000 + myId
    server = (host, port)
    # bind a socket for UDP listener
    s_socket.bind(server)

    while not FINISH:
        # check FINISH condition every 10 sec
        s_socket.settimeout(10.0)
        try:
            recvPing, addr = s_socket.recvfrom(1024)
        except socket.timeout:
            continue
        
        s_socket.settimeout(None)
        recvPing = pickle.loads(recvPing)
        recvMsg = recvPing.msg
        srcId = recvPing.id
        flag = recvPing.flag
        srcPos = recvPing.myPos

        print('------------UDP Listener thread----------')

        if flag == 'RESPONSE':
            lastPing[recvPing.myPos] = recvPing.seq
            print(recvMsg)
            
            # Succ2 died, request info from Succ1
            if lastPing['Succ1'] - lastPing['Succ2'] > 4:
                print(f"Peer {mySucc2} is no longer alive.")
                sendData = TCPMsg(myId, INFO_REQUEST, 'Prev1', mySucc2)
                sendTCPMsg(pickle.dumps(sendData), mySucc1)
                # balance last ping to avoid further change
                lastPing['Succ2'] = lastPing['Succ1']
                
            # Succ1 died, request info from Succ2
            if lastPing['Succ2'] - lastPing['Succ1'] > 4:
                print(f'Peer {mySucc1} is no longer alive.')
                sendData = TCPMsg(myId, INFO_REQUEST, 'Prev2', mySucc1)
                sendTCPMsg(pickle.dumps(sendData), mySucc2)
                # balance last ping to avoid further change
                lastPing['Succ1'] = lastPing['Succ2']
                

        elif flag == 'REQUEST':
            print(recvMsg)
            print(f'received from Peer {srcId}, which is my {srcPos}')

            updatePrev(srcId, srcPos)
            print(f"Peer {myId}: [Prev1: {myPrev1}] [Prev2: {myPrev2}]")
            print(f"Peer {myId}: [Succ1: {mySucc1}] [Succ2: {mySucc2}]")
            respPing = copy.deepcopy(recvPing)
            respPing.flag = 'RESPONSE'
            if srcPos == 'Prev1':
                respPing.myPos = 'Succ1'
            elif srcPos == 'Prev2':
                respPing.myPos = 'Succ2'
            respPing.id = myId
            sendUDPMsg(pickle.dumps(respPing), srcId)

        print(f'lastPing: {lastPing}')

        print('--------------------------------------\n')
        #time.sleep(7)
    print("UDPListener exiting...")
    s_socket.close()

def TCPHandler():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH

    print(f'TCP handler thread with id {myId}: Start listening')
    logging.debug('running with %s', myId)

    # create socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('localhost', 50000+myId))

    while not FINISH:
        # check FINISH condition every 10 sec
        listen_socket.settimeout(10.0)
        try:
            print('=============TCP Handler retry============')
            listen_socket.listen(1)
            conn, addr = listen_socket.accept()
            # connection socket
        except socket.timeout:
            continue
        
        listen_socket.settimeout(None)
        print('--------------TCP Handler thread----------------')

        print(f'Peer {myId}: Connection from {addr}')
        # receive data from connection socket
        recvData = pickle.loads(conn.recv(1024))
        print(f'received "{str(recvData)}"')
        srcId = recvData.id
        srcFlag = recvData.flag
        srcPos = recvData.myPos
        srcMsg = recvData.msg
        print(f'received Peer: {srcId}')
        print(f'received flag: {srcFlag}')
        print(f'received position: {srcPos}')
        print(f'received msg: {srcMsg}')

        # sending/forwarding reqeust for file
        if srcFlag is FILE_REQUEST:
            file = int(srcMsg.split()[0])
            fileName = srcMsg.split()[1]
            # extract file name
            has = checkFile(file)
            print(f"Looking for file {fileName}")
            # if self has the file, connect and send response directly to requesting peer
            if has:
                msg = f'{file} {fileName}'
                respData = TCPMsg(myId, FILE_RESPONSE, None, msg)
                sendTCPMsg(pickle.dumps(respData), srcId)
                print(f"File {fileName} is stored here.\nA response message, destined for peer {srcId}, has been sent.")

            # if self doesn't has file, connect and send request next peer
            elif not has:
                print(f"File {fileName} is not stored here.")
                sendTCPMsg(pickle.dumps(recvData), mySucc1)
                print("File request message has been forwarded to my successor.")

        # when the file holder send back response to requesting peer
        elif srcFlag is FILE_RESPONSE:
            file = int(srcMsg.split()[0])
            fileName = srcMsg.split()[1]
            respondingPeer = srcId
            print(f"Received a response message from peer {respondingPeer}, which has the file {fileName}.")

        # when the peer is leaving
        elif srcFlag is QUIT_NOTIFY:
            msg = srcMsg.split()
            leavingPeer = recvData.myPos
            assert(len(msg) >= 2)
            new_Succ1 = int(msg[0])
            new_Succ2 = int(msg[1])

            # if leaving peer is mySucc1, update both
            if leavingPeer == 'Succ1':
                updateNext(new_Succ1, new_Succ2)

            # if leaving peer is mySucc2, only update mySucc2
            elif leavingPeer == 'Succ2':
                updateNext(None, new_Succ1)


            depart_msg = ' '.join(msg[2:])
            print(depart_msg)

        # when someone is dead and its predecessor requesting for my info
        elif srcFlag is INFO_REQUEST:
            assert (srcMsg is not None)
            deadPeer = int(srcMsg)
            # if the dead peer still in my successors, ignore
            if (srcId == myPrev1) and (deadPeer in [mySucc1, mySucc2]):
                pass
            else:
                mySuccessors = f'{mySucc1} {mySucc2}'
                if srcPos == 'Prev1':
                    myPos = 'Succ1'
                elif srcPos == 'Prev2':
                    myPos = 'Succ2'

                sendData = TCPMsg(myId, INFO_RESPONSE, myPos, mySuccessors)
                sendTCPMsg(pickle.dumps(sendData), srcId)

        # when a peer respond to my INFO_REQUEST, update my Succ
        elif srcFlag is INFO_RESPONSE:
            print('============get INFO_RESPONSE==========')
            new_Succ1 = int(srcMsg.split()[0])
            new_Succ2 = int(srcMsg.split()[1])

            # if responding peer is mySucc1, make its Succ1 be mySucc2
            if srcPos == 'Succ1':
                print('Updating Succ1...')
                updateNext(None, new_Succ1)

            # if responding peer is mySucc2, make it mySucc1 and make its Succ1 be mySucc2
            elif srcPos == 'Succ2':
                print('Updating Succ2...')
                updateNext(mySucc2, new_Succ1)

        conn.close()
        print("-------------------------------------\n")

    print("TCPHandler exiting...")
    listen_socket.close()

# initialise threads
# tInputMonitor = threading.Thread(target=inputMonitor)
tpingSender = threading.Thread(target=pingSender)
tUDPListener = threading.Thread(target=UDPListener)
tTCPHandeler = threading.Thread(target=TCPHandler)

# start all threads
# tInputMonitor.start()
time.sleep(3)
tpingSender.start()
tUDPListener.start()
tTCPHandeler.start()

while(True):
    try:
        s = input()
        print("get input " + s)
    except KeyboardInterrupt:
        FINISH = True
        for t in [tpingSender, tUDPListener, tTCPHandeler]:
            t.join()
        break
    else:
        try:
            flag = s.split()[0]
            print(f"flag is: {flag}")
        except:
            print('invalid')
            continue
        else:
            if flag == 'request':
                try:
                    fileName = s.split()[1]
                    file = validateFileName(s)
                except (IndexError, ValueError) as er:
                    print(er)
                    continue
                else:
                    print(f'successfully validate file {fileName}')
                    print(f'preparing to send to {myId}')
                    sendData = TCPMsg(myId, FILE_REQUEST, None, f'{file} {fileName}')
                    print(f'sendData: {sendData}')
                    sendTCPMsg(pickle.dumps(sendData), myId)
                    print(f'successfully send to Peer {myId}')

            elif flag == 'quit':
                    mySuccessors = f'{mySucc1} {mySucc2}'
                    msg = f'{mySuccessors} Peer {myId} will depart from the network.'
                    sendData_toPrev1 = TCPMsg(myId, QUIT_NOTIFY, 'Succ1', msg)
                    sendData_toPrev2 = TCPMsg(myId, QUIT_NOTIFY, 'Succ2', msg)

                    sendTCPMsg(pickle.dumps(sendData_toPrev1), myPrev1)
                    sendTCPMsg(pickle.dumps(sendData_toPrev2), myPrev2)

                    print("\n----time to kill myself-----")
                    FINISH = True
                    time.sleep(1)
                    for t in [tpingSender, tUDPListener, tTCPHandeler]:
                        t.join()
                    break

            else:
                print('try again')


print("\n--------all thread ended--------")

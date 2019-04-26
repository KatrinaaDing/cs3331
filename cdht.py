# python 3.7.2
import time
import random
import socket
import pickle, itertools
import threading
import sys
import time
import copy

startTime = time.time()

FILE_REQUEST = 2        # requesting a file
FILE_RESPONSE = 1       # responding to requesting peer that I have the file
QUIT_NOTIFY = 3         # notifying others that I'm leaving
INFO_REQUEST = 4        # requesting my successors infomation
INFO_RESPONSE = 5       # response to INFO_REQUEST
FINISH = False          # flag to stop all threa

#for data transfer
ACK = 100               # is sent by receiver
PAYLOAD = 200           # is sent by sender
FIN = 300               # is sent by sender, notifying that all data are sent
FINACK = 400            # is sent by receiver, notifying that it has received the FIN
FINBIT = 1

targetFile = None       # the file to send/receive

# for sender (file holder)      # reason having seperate:
IM_SENDER = False               # a peer might be both sender and receiver
theReceiver = -1
lastSentSeq = -1
lastRecvAck = -1

# for receiver (reqeusitng peer)
IM_RECEIVER = False
theSender = -1
lastRecvSeq = -1
lastSentAck = -1

myId = int(sys.argv[1])         # read my id from command line
mySucc1 = int(sys.argv[2])      # read my first successor
mySucc2 = int(sys.argv[3])      # read my second successor
myPrev1 = None                  # first predecessor will be known from ping reqeust
myPrev2 = None                  # second predecessor will be known from ping request
MSS = int(sys.argv[4])          # read Maximum Segment Size from command line
dropRate = float(sys.argv[5])   # read drop rate from command line

# some assertion for correct input
assert(type(myId) is int and myId >= 0 and myId <= 255)
assert(type(mySucc1) is int and mySucc1 >= 0 and mySucc1 <= 255)
assert(type(mySucc2) is int and mySucc2 >= 0 and mySucc2 <= 255)
assert(dropRate >= 0 and dropRate <= 1)

print(f'Seting up peer with id {myId}...')

# a template for Ping msg
class PingMsg:
    def __init__(self, seq, id, flag, myPos):
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

# a template for TCP msg
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

# a template for File msg (both segment and ACK)
# (seq is None and content is None) when (flag==ACK or flag==FINACK)
# ACK is None  when (flag==PAYLOAD or flag==FIN)
class FileSegment:
    def __init__(self, seq, ack, flag, content, mss):
        self._seq = seq
        self._ack = ack
        self._flag = flag
        self._content = content
        self._mss = mss

    @property
    def seq(self):
        return self._seq

    @property
    def ack(self):
        return self._ack

    @property
    def flag(self):
        return self._flag

    @property
    def content(self):
        if self._content is None:
            return b""
        else:
            return self._content

    @property
    def mss(self):
        return self._mss

    def __str__(self):
        msg = f"[File Segment] Seq: {self._seq}, ACK: {self._ack}, Flag: {self._flag}, MSS: {self._mss}\nContent: {self._content}"
        return msg

# validate file name input, raise Error if file name not valid
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

# check if I have the file
def checkFile(file):
    global myId, myPrev1, myPrev2

    assert(type(file) is int and file >= 0 and file <= 9999)
    expectedPeer = hashFunc(file)
    assert(type(expectedPeer) is int)

    if myId == expectedPeer:
        return True

    elif myId > myPrev1:
        if (myId >= expectedPeer) and (myPrev1 < expectedPeer):
            return True
        else:
            return False

    # if I'm the first peer in the dht
    elif myId < myPrev1 and myId < myPrev2:
        if myId >= expectedPeer or (expectedPeer > myPrev1) :
            return True
        else:
            return False

# hash function for calculating expected file holder
def hashFunc(file):
    assert(type(file) is int and file >= 0 and file <= 9999)
    hash = file % 256
    return hash

# function to update predecessors
def updatePrev(srcId, srcPos):
    global myPrev1, myPrev2

    assert(type(srcId) is int)
    if srcPos == 'Prev1':
        myPrev1 = srcId
    elif srcPos == 'Prev2':
        myPrev2 = srcId
    else:
        print("fail to update prev")

# function to update successors
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

# send TCP Message from random port (by TCP)
def sendTCPMsg(msg, destId):
    destId = int(destId)
    destPort = 50000 + destId # will be reset after demo
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        send_socket.connect(('localhost', destPort))
        send_socket.send(msg)

    # try again if connection refused
    except:
        # print("connection refused, ready to try again")
        time.sleep(1)
        send_socket.connect(('localhost', destPort))
        send_socket.send(msg)
    send_socket.close()

# send Ping Message from random Port (by UDP)
def sendPingMsg(msg, destId):
    global myId, mySucc1, mySucc2, myPrev1, myPrev2

    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # will be reset to 50000+id after demo
    destPort = 50000 + destId
    destServer = ('localhost', destPort)
    c_socket.sendto(msg, destServer)

    c_socket.close()

# send File Segment and ACK from random Port (by UDP)
def sendFileMsg(msg, destId, resend = False):
    global lastSentSeq, lastRecvAck
    # as assignmetn doesn't specify a port for file transfer,
    # make id+60256 be port to receive file msg
    destPort = int(destId) + 60256
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    extract = pickle.loads(msg)
    if IM_SENDER:
        role = 'sender'
    if IM_RECEIVER:
        role = 'receiver'

    rand = random.random()
    if rand >= dropRate:
        destServer = ('localhost', destPort)

        if resend == True and IM_SENDER:
            recordLog('sender', 'RTX', (time.time()-startTime), extract.seq, len(extract.content), extract.ack)
        else:
            recordLog(role, 'Snd', (time.time()-startTime), extract.seq, len(extract.content), extract.ack)

        c_socket.sendto(msg, destServer)

    else:
        # print(f"\n---------<<File Pkt LOST>> dest to {destId}--------\n")
        if resend == True:
            recordLog(role, 'drop/RTX', (time.time()-startTime), extract.seq, len(extract.content), extract.ack)
        else:
            recordLog(role, 'drop', (time.time()-startTime), extract.seq, len(extract.content), extract.ack)

# function to record log.txt file
def recordLog(role, event, time, seq, dataNum, ack):
    if len(event) == 3:
        event = f'{event} '
    if len(str(seq)) == 3:
        seq = f'{seq} '

    if role == 'sender':
        respondLog_fp = open('responding_log.txt', 'a')
        respondLog_fp.write('%-10s %5.6f\t%-10s %-10s %-10s\n' % (event,time,seq,dataNum,ack))
        respondLog_fp.close()

    elif role == 'receiver':
        requestLog_fp = open('requesting_log.txt', 'a')
        requestLog_fp.write('%-10s %5.6f\t%-10s %-10s %-10s\n' % (event,time,seq,dataNum,ack))
        requestLog_fp.close()

'''
Threading function
'''
# thread that handle file transfering. Only start when a file request/response are successfully received
def FileHandler():
    global myId, targetFile, MSS, theReceiver, theSender, lastSentSeq, lastRecvAck, lastRecvSeq,lastSentAck, IM_SENDER, IM_RECEIVER, FINISH

    print(f"Peer {myId}: File Handler thread started")
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = 'localhost'
    port = 60256 + myId
    server = (host, port)
    s_socket.bind(server)

    lastPkt = None
    retransmit = 0

    fileToRead = f'{targetFile}.pdf'
    fileToWrite = f'received_file.pdf'

    # send first payload if I'm sender
    if IM_SENDER and lastSentSeq < 0:
        print("We now start sending the file ......")
        try:
            fp_read = open(fileToRead, 'rb')
        except:
            print('No such file')

        chunk = fp_read.read(MSS)
        initialSeqNum = random.randint(100, 1000)
        # wait for receiver for 1 sec to open socket
        time.sleep(1)
        sendPkt = FileSegment(initialSeqNum, None, PAYLOAD, chunk, MSS)
        sendFileMsg(pickle.dumps(sendPkt), theReceiver)
        # print(f'Send pkt: {sendPkt}')

        lastPkt = sendPkt
        lastSentSeq = initialSeqNum

    if IM_RECEIVER:
        print(f"We now start receiving the file ......")
        fp_write = open(fileToWrite, 'ab')

    while not FINISH:
        # send first payload
        s_socket.settimeout(1.0)
        try:
            recvPkt, addr = s_socket.recvfrom(1024)

        # resend if timeout
        except socket.timeout:
            if IM_SENDER and lastPkt is not None:
                if retransmit > 4:
                    # print("retransmit 5 times already")
                    break

                sendFileMsg(pickle.dumps(lastPkt), theReceiver, True)
                # print(f"Resend pkt: {lastPkt}")
                retransmit += 1
                continue
            else:
                continue

        # reset retransmiting time
        retransmit = 0
        # extract information
        recvPkt = pickle.loads(recvPkt)
        srcSeq = recvPkt.seq
        srcAck = recvPkt.ack
        srcFlag = recvPkt.flag
        srcContent = recvPkt.content

        # if the file holder get an ACK, send file payload
        if srcFlag == ACK:
            assert(IM_SENDER)
            recordLog('sender', 'rcv', (time.time()-startTime), srcSeq, len(srcContent), srcAck)
            #print("I'm Sender:")

            if srcAck > lastRecvAck:
                if srcAck == (lastSentSeq + len(lastPkt.content)):
                    newSeq = srcAck
                    lastRecvAck = srcAck
                    chunk = fp_read.read(MSS)
                    # if reach the end of the file
                    if chunk == b'':
                        print("All data has been read. Send FIN.")
                        respMsg = FileSegment(newSeq, None, FIN, None, MSS)

                    else:
                        respMsg = FileSegment(newSeq, None, PAYLOAD, chunk, MSS)

                    sendFileMsg(pickle.dumps(respMsg), theReceiver)

                    # print(f'Send pkt: {respMsg}')
                    lastSentSeq = newSeq
                    lastPkt = respMsg
                else:
                    print("!!!! ERROR: Received unexpected ACK")
            else:
                print("srcACK =< lastRecvAck, ignore")

        # if the reqeusting file get a PAYLOAD, load the payload and respond with ACK
        elif srcFlag == PAYLOAD:
            assert(IM_RECEIVER)
            recordLog('receiver', 'rcv', (time.time()-startTime), srcSeq, len(srcContent), srcAck)
            # print("I'm Receiver: ")

            # detect duplicate, ignore payload and resend ACK
            if srcSeq == lastRecvSeq:
                respMsg = FileSegment(None, lastSentAck, ACK, None, MSS)
                sendFileMsg(pickle.dumps(respMsg), theSender)


            # receive payload, load chunk and send ACK
            elif srcSeq >= lastSentAck:
                lastRecvSeq = srcSeq
                newAck = srcSeq + len(srcContent)

                fp_write.write(srcContent)
                respMsg = FileSegment(None, newAck, ACK, None, MSS)
                sendFileMsg(pickle.dumps(respMsg), theSender)

                lastSentAck = newAck
            else:
                print("!!!!!! ERROR: srcSeq < lastRecvSeq")

        # if all data has been transfered and sender send FIN to receiver
        elif srcFlag == FIN:
            assert(IM_RECEIVER)
            recordLog('receiver', 'rcv', (time.time()-startTime), srcSeq, len(srcContent), srcAck)
            # print("All data has finished transfering, send back FINACK")

            lastRecvSeq = srcSeq
            newAck = srcSeq + FINBIT
            respMsg = FileSegment(None, newAck, FINACK, None, MSS)
            sendFileMsg(pickle.dumps(respMsg), theSender)
            lastPkt = respMsg
            break

        # sender received a FINACK
        elif srcFlag == FINACK:
            assert(IM_SENDER)
            recordLog('sender', 'rcv', (time.time()-startTime), srcSeq, len(srcContent), srcAck)
            # print("Get FINACK")
            break

        else:
            print("!!!!! ERROR: Fail to identify file Segment flag")


    if IM_SENDER:
        print("The file is sent.")
        fp_read.close()
    elif IM_RECEIVER:
        print("The file is received.")
        fp_write.close()

    print("File Handler exiting...")
    s_socket.close()

# thread that pings successors every 40 seconds
def pingSender():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, FINISH
    print("UDP Sender thread: start sending ping")
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
            sendPingMsg(send_data, s)
            # print(f'------------Sending Ping to Peer {s}------------\n')

        seqNum += 1
        time.sleep(20)

    print("pingSender exiting...")

# thread that listen for UDP Msg, check FINISH flag every 10 second
def pingListener():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, MSS, FINISH
    lastPing = {'Succ1': 0, 'Succ2': 0}
    print('UDP Listener thread: UDP server with id ' + str(myId) + ' started')

    s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = 'localhost'
    port = 50000 + myId # will be reset after demo
    server = (host, port)
    # bind a socket for UDP listener
    s_socket.bind(server)

    while not FINISH:
        # check FINISH condition every 10 sec
        s_socket.settimeout(10.0)
        try:
            recvPkt, addr = s_socket.recvfrom(1024)
        except socket.timeout:
            continue

        s_socket.settimeout(None)
        recvPkt = pickle.loads(recvPkt)

        recvPing = recvPkt
        recvMsg = recvPing.msg
        srcId = recvPing.id
        flag = recvPing.flag
        srcPos = recvPing.myPos

        if flag == 'RESPONSE':
            lastPing[recvPing.myPos] = recvPing.seq
            print(recvMsg)

            # Succ2 died, request info from Succ1
            if lastPing['Succ1'] - lastPing['Succ2'] > 3:
                print(f"Peer {mySucc2} is no longer alive.")
                sendData = TCPMsg(myId, INFO_REQUEST, 'Prev1', mySucc2)
                sendTCPMsg(pickle.dumps(sendData), mySucc1)

                # balance last ping to avoid further change
                # and will re-request again if I didn't update
                # my successors info successfully
                lastPing['Succ2'] += 2

            # Succ1 died, request info from Succ2
            if lastPing['Succ2'] - lastPing['Succ1'] > 3:
                print(f'Peer {mySucc1} is no longer alive.')
                sendData = TCPMsg(myId, INFO_REQUEST, 'Prev2', mySucc1)
                sendTCPMsg(pickle.dumps(sendData), mySucc2)

                # balance last ping to avoid further change
                # and will re-request again if I didn't update
                # my successors info successfully
                lastPing['Succ1'] += 2

        elif flag == 'REQUEST':
            print(recvMsg)

            updatePrev(srcId, srcPos)
            respPing = copy.deepcopy(recvPing)
            respPing.flag = 'RESPONSE'
            if srcPos == 'Prev1':
                respPing.myPos = 'Succ1'
            elif srcPos == 'Prev2':
                respPing.myPos = 'Succ2'
            respPing.id = myId
            sendPingMsg(pickle.dumps(respPing), srcId)


        # print(f"\nPeer {myId}: [Prev1: {myPrev1}] [Prev2: {myPrev2}]")
        # print(f"Peer {myId}: [Succ1: {mySucc1}] [Succ2: {mySucc2}]")
        # print(f'lastPing: {lastPing}')

    print("pingListener exiting...")
    s_socket.close()

# thread that listen for TCP Msg, check FINISH flag every 10 second
def TCPHandler():
    global myId, mySucc1, mySucc2, myPrev1, myPrev2, MSS, IM_SENDER, IM_RECEIVER, theSender, theReceiver, targetFile, FINISH

    print(f'TCP handler thread with id {myId}: Start listening')

    # create socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('localhost', 50000+myId))   # will reset after demo

    while not FINISH:
        # check FINISH condition every 10 sec
        listen_socket.settimeout(10.0)
        try:
            listen_socket.listen(1)
            conn, addr = listen_socket.accept()
            # connection socket
        except socket.timeout:
            continue

        listen_socket.settimeout(None)

        # receive data from connection socket
        recvData = pickle.loads(conn.recv(1024))
        srcId = recvData.id
        srcFlag = recvData.flag
        srcPos = recvData.myPos
        srcMsg = recvData.msg
        # print(f'received from Peer {srcId}')

        # sending/forwarding reqeust for file
        if srcFlag is FILE_REQUEST:
            file = int(srcMsg.split()[0])
            fileName = srcMsg.split()[1]
            # extract file name
            has = checkFile(file)
            # print(f"Looking for file {fileName}")
            # if self has the file, connect and send response directly to requesting peer
            if has:
                try:
                    fp = open(f'{fileName}.pdf', 'r')
                except:
                    print("!!!!!! Error: Sorry, the file is not exist")
                else:
                    fp.close()
                    msg = f'{file} {fileName}'
                    respData = TCPMsg(myId, FILE_RESPONSE, None, msg)
                    sendTCPMsg(pickle.dumps(respData), srcId)
                    print(f"File {fileName} is stored here.\nA response message, destined for peer {srcId}, has been sent.")

                    # start sending file
                    IM_SENDER = True
                    theReceiver = srcId
                    targetFile = fileName
                    tFileHandler.start()

            # if self doesn't has file, connect and send request next peer
            elif not has:
                print(f"File {fileName} is not stored here.")
                sendTCPMsg(pickle.dumps(recvData), mySucc1)
                print("File request message has been forwarded to my successor.")

        # when receives file holder's response to requesting peer
        elif srcFlag is FILE_RESPONSE:
            file = int(srcMsg.split()[0])
            fileName = srcMsg.split()[1]
            respondingPeer = srcId
            print(f"Received a resposnse message from peer {respondingPeer}, which has the file {fileName}.")
            IM_RECEIVER = True
            theSender = respondingPeer
            targetFile = fileName
            # start receiving files
            try:
                tFileHandler.start()
            except:
                pass

        # when the peer is leaving
        elif srcFlag is QUIT_NOTIFY:
            msg = srcMsg.split()
            leavingPeer = recvData.myPos
            assert(len(msg) >= 2)
            new_Succ1 = int(msg[0])
            new_Succ2 = int(msg[1])
            depart_msg = ' '.join(msg[2:])

            print(depart_msg)

            # if leaving peer is mySucc1, update both
            if leavingPeer == 'Succ1':
                updateNext(new_Succ1, new_Succ2)

            # if leaving peer is mySucc2, only update mySucc2
            elif leavingPeer == 'Succ2':
                updateNext(None, new_Succ1)

        # when someone is dead and its predecessor requesting for my info
        elif srcFlag is INFO_REQUEST:
            assert (srcMsg is not None)
            deadPeer = int(srcMsg)
            # if the dead peer still in my successors, ignore
            # the predecessor will re-send INFO_REQUEST when it finds its
            # successor is dead.
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
            new_Succ1 = int(srcMsg.split()[0])
            new_Succ2 = int(srcMsg.split()[1])

            # if responding peer is mySucc1, make its Succ1 be mySucc2
            if srcPos == 'Succ1':
                updateNext(None, new_Succ1)

            # if responding peer is mySucc2, make it mySucc1 and make its Succ1 be mySucc2
            elif srcPos == 'Succ2':
                updateNext(mySucc2, new_Succ1)

        conn.close()

    print("TCPHandler exiting...")
    listen_socket.close()

# initialise threads
tpingSender = threading.Thread(target=pingSender)
tpingListener = threading.Thread(target=pingListener)
tTCPHandeler = threading.Thread(target=TCPHandler)
tFileHandler = threading.Thread(target=FileHandler)

# start all threads
time.sleep(2)
tpingListener.start()
tpingSender.start()
tTCPHandeler.start()

# Input monitor, handleing 'request' and 'quit. Ignore if input is invalid
while(True):
    try:
        s = input()
        print("get input " + s)
    except KeyboardInterrupt:
        FINISH = True
        for t in [tpingSender, tpingListener, tTCPHandeler]:
            t.join()
        break
    else:
        try:
            flag = s.split()[0]
            # print(f"flag is: {flag}")
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
                    # print(f'successfully validate file {fileName}')
                    # print(f'preparing to send to {myId}')
                    sendData = TCPMsg(myId, FILE_REQUEST, None, f'{file} {fileName}')
                    # print(f'sendData: {sendData}')
                    sendTCPMsg(pickle.dumps(sendData), myId)
                    # print(f'successfully send to Peer {myId}')

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
                    for t in [tpingSender, tpingListener, tTCPHandeler]:
                        t.join()
                    break

            else:
                print('try again')

print("\n--------all thread ended--------")
exit()
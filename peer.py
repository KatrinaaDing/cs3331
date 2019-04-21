import socket
import random
import threading
import time
import logging

'''
header: "id port-to-listen"
'''
FILE_REQUEST = 2
FILE_RESPONSE = 1
QUIT_NOTIFY = 3

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class Peer(threading.Thread):

    def __init__(self, id, next, secNext, dropRate):
        threading.Thread.__init__(self)
        self._id = int(id)
        self._next = int(next)
        self._secNext = int(secNext)
        self._prev = None
        self._secPrev = None
        self._dropRate = float(dropRate)
        self._UDPheader = f'{self._id} {self._id+50000}' # UDPheader: id port-to-listen
        #self._TCPheader = f'{self._id} {self._id+50000}'
        assert(type(self._id) is int and self._id >= 0 and self._id <= 255)
        assert(type(self._next) is int and self._next >= 0 and self._next <= 255)
        assert(type(self._secNext) is int and self._secNext >= 0 and self._secNext <= 255)
        assert(self._dropRate >= 0 and self._dropRate <= 1)
    
    # check if self is the one having file
    print("My first successor is now peer {self.next}")
    def checkFile(self, file):
        assert(type(file) is int and file >= 0 and file <= 9999)
        expectedPeer = self.hashFunc(file)
        assert(type(expectedPeer) is int)
        if self.id >= expectedPeer:
            return True
        else: 
            return False
        
    def hashFunc(self, file):
        assert(type(file) is int and file >= 0 and file <= 9999)
        hash = file % 256
        return hash
    
    def extractHeader(self, protocol, msg):
        msg = msg.split()
        if protocol is 'UDP':
            headerSize = 2
        elif protocol is 'TCP':
            headerSize = 3
        
        header = msg[0:headerSize]
        msg = ' '.join(msg[headerSize:])
        return (header,msg)
        
    def TCPheader(self, flag):
        header = self.UDPheader + f' {flag}'
        check = header.split()
        assert(len(check) == 3)    
        return header
    
    def updatePrev(self, srcId):
        print(f'srcId is {srcId}, type is {type(srcId)}')
        assert(type(srcId) is int)
        if srcId in [self.secPrev, self.prev]:
            print("updatePrev: srcId already in prev")
            return True

        assert (srcId not in [self.secPrev, self.prev])
        
        if self.prev is None or self.secPrev is None:
            print('one of prev is None')
            if self.prev is None:
                print('prev is None, now set prev=srcId')
                self.prev = srcId
            elif self.secPrev is None:
                print('secprev is None, now set secPrev=srcId')
                self.secPrev = srcId
        else:
            print('both prev are not None')
            if self.secPrev > self.prev:
                print('found that secPrive > prev, exchange')
                tmp = self.prev
                self.prev = self.secPrev
                self.secPrev = tmp
            assert (self.prev > self.secPrev)
            
            if (srcId > self.prev):
                print('srcId > prev, replace prev')
                self.secPrev = self.prev
                self.prev = srcId
                return True
            
            elif (srcId < self.prev) and (srcId > self.secPrev):
                print('secPrev < srcId < prev, replace secPrev')
                self.secPrev = srcId
                return True
            
        # should never get to this stage
        assert(False)
    
    def updateNext(self, new_next, new_secNext):
        new_next = int(new_next)
        new_secNext = int(new_secNext)
        assert(new_secNext > new_next)
        
        self.next = new_next
        self.secNext = new_secNext
        print(f"My first successor is now peer {self.next}.")
        print(f"My second successor is now peer {self.secNext}.")
        
    def notifyDepart(self, id):
        print(f'Peer {id} will depart from the network.')


    def __str__(self):
        msg = f"[Peer {self.id}] with [Succ {self.next} and [secSucc {self.secNext}]]"
        return msg

    '''
    Properties
    '''
    @property
    def id(self):
        return self._id

    @property
    def next(self):
        return self._next

    @property
    def secNext(self):
        return self._secNext

    @property
    def prev(self):
        return self._prev
    @property
    def secPrev(self):
        return self._secPrev
    
    @property
    def dropRate(self):
        return self._dropRate 
    
    @property
    def UDPheader(self):
        return self._UDPheader
    '''
    Setters
    '''

    @next.setter
    def next(self, successor):
        self._next = successor

    @secNext.setter
    def secNext(self, secNext):
        self._secNext = secNext

    @prev.setter
    def prev(self, predecessor):
        self._prev = predecessor
        
    @secPrev.setter
    def secPrev(self, secPrev):
        self._secPrev = secPrev
        
class UDPSender(Peer):
    def run(self):
        print("UDP Sender thread: start sending ping")
        logging.debug('running with %s', self.id)
        while True:
            sendMsg = "A ping request message was received from Peer " + str(self.id)
            c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            header = self.UDPheader
            for s in [self.next, self.secNext]:
                sendMsg = f'{header} [UDP client {s}] A ping request was received from Peer {self.id}.'
                rand = random.randint(0, 10)
                if rand >= self.dropRate:
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
            
class UDPListener(Peer):

    def run(self):
        print('UDP Listener thread: UDP server with id ' + str(self.id) + ' started')
        logging.debug('running with %s', self.id)
        while True:
            s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host = 'localhost'
            port = 50000 + self.id
            server = (host,port)
            # bind a socket for UDP listener
            s_socket.bind(server)
           
            recvMsg, srcAddr = s_socket.recvfrom(1024)
            recvMsg = recvMsg.decode('utf-8')
            header, msg = self.extractHeader('UDP', recvMsg)
            srcId = int(header[0])
            # srcPort = int(recvMsg[1])
            # srcAddr = ('localhost', srcPort)
            print('Listener thread: [UDP server ' + str(self.id) + ']' + 'received msg: ' + msg)
            if "response" in recvMsg:
                pass
            elif "request" in recvMsg:
                print(f'Listener thread: received from Peer {srcId}')
                try:
                    self.updatePrev(srcId)
                except:
                    print(f"Peer {self.id}: fail to update prev and secPrev")
                    
                print(f"Peer {self.id}: [Prev: {self.prev}] [nextPrev: {self.secPrev}]")
                sendMsg = f"A ping response message was received from Peer {self.id}."
                s_socket.sendto(sendMsg.encode('utf-8'), srcAddr)

class TCPHandler(Peer):
    
    def sendMsg(self, msg, destPort):
        destPort = int(destPort)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_socket.connect(('localhost', destPort))
        send_socket.send(msg.encode('utf-8'))
        send_socket.close()
        
    def run(self):
        print(f'TCP handler thread with id {self.id}: Start listening')
        logging.debug('running with %s', self.id)
        
        # create socket
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind(('localhost', 50000+self.id))
        
        while(True):
            listen_socket.listen(1)
            # connection socket
            conn, addr = listen_socket.accept()
            print(f'TCP handler thread widh id {self.id}: Connection from {addr}')
            # receive data from connection socket
            data = conn.recv(1024).decode('utf-8')
            print(f'TCP handler thread with id {self.id}: received "{data}"')
            header, recvMsg = self.extractHeader("TCP", data)
            print(f'TCP handler received data: {data}')
            print(f'TCP handler received header: {header}')
            print(f'TCP handler received recvMsg: {recvMsg}')
            file = int(recvMsg.split()[0])
            msgType = int(header[2])
            # sending/forwarding reqeust for file
            if msgType is FILE_REQUEST:
                # extract file name
                has = self.checkFile(file)
                # if self has the file, connect and send response directly to requesting peer
                if has:
                    requestingPeer = header[0]
                    requestingPort = header[1]
                    TCPheader = self.TCPheader(FILE_RESPONSE)
                    msg = TCPheader + f' {file}'
                    self.sendMsg(msg, requestingPort)
                    print(f"TCP handler: File {file} is stored here.\nA response message, destined for peer {requestingPeer}, has been sent.")
                    
               # if self doesn't has file, connect and send request next peer
                elif not has:
                    print(f"TCP handler: File {file} is not stored here.")
                    nextPort = self.next + 50000
                    msg =  ' '.join(header) + f' {file}'
                    self.sendMsg(msg, nextPort)
                    print("TCP handler: File request message has been forwarded to my successor.")
                    
            # when the file holder send back response to requesting peer  
            elif msgType is FILE_RESPONSE:
                respondingPeer = header[0]
                print(f"TCP handler: Received a response message from peer {respondingPeer}, which has the file {file}.")
            
            # when the peer is leaving 
            elif msgType is QUIT_NOTIFY:
                recvMsg = recvMsg.split()
                assert(len(recvMsg) == 2)
                new_next = recvMsg[0]
                new_secNext = recvMsg[1]
                depart_msg = ' '.join(recvMsg[2:])
                print(depart_msg)
                self.updateNext(new_next, new_secNext)
                
                
            conn.close()
                

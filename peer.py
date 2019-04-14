import socket
import random

class Peer():

    def __init__(self, id):
        self._id = int(id)
        self._next = None
        self._secNext = None
        self._prev = None
        assert(type(id) is int and id >= 0 and id <= 255)

    def sendPing(self):
        srcAddr = 'localhost'
        srcPort = 50000 + self.id
        client = (srcAddr, srcPort)
        
        sendMsg = "A ping request message was received from Peer " + str(self.id)
        for s in [self.next, self.secNext]:    
            # UDP only need 1 socket, destAddr, destport
            destAddr = 'localhost'
            destPort = 50000 + s.id
            server = (destAddr, destPort)
            # create a client socket
            c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # bind the socket to the client port
            c_socket.bind(client)
            # send ping request and set timmer to 6s
            sendMsg = '[UDP client id ' + str(s.id) + ']' + "A ping request was received from Peer " + str(self.id) + "."
            # generate random number and simualte pkt loss
            rand = random.randint(0, 10)
            if rand >= 4:
                c_socket.sendto(sendMsg.encode('utf-8'), server)
                c_socket.settimeout(1.0)  

                try:
                    data, serverAddr = c_socket.recvfrom(1024) 
                    # print("Ping to " + s.id + ', port: ' + port + ', with msg: ' + sendMsg)
                    # print(data)
                except socket.timeout:
                    print('[UDP client id ' + str(self.id) + ']' + "<PACKET LOST> Ping to " +
                        str(s.id) + ', port: ' + str(destPort))

                else:
                    #print('UDPclient id ' + s.id + ']' + "Client received msg: " + data.decode('utf-8'))
                    print('[UDP client id ' + str(self.id) + ']' + "A ping response was received from: " +
                        serverAddr + ", data: " + data.decode('utf-8'))
            c_socket.close()
                
    def listenPing(self):
        s_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        host = 'localhost'
        port = 50000 + self.id
        server = (host,port)
        # bind a socket for UDP
        s_socket.bind(server)
        print('UDP server with id ' + str(self.id) + ' started')
        
        s_socket.settimeout(2)
        try:
            recvMsg, client = s_socket.recvfrom(1024)
            
        except socket.timeout:
            pass
        else:    
            print('[UDP server id ' + str(self.id) + ']' + 'received msg: ' + recvMsg.decode('utf-8'))
            if "response" in recvMsg:
                pass
            elif "request" in recvMsg:
                print(recvMsg.decode('utf-8'))
                sendMsg = "A ping response message was received from Peer " + str(self.id)
                s_socket.sendto(sendMsg, client)
        #s_socket.close()
        '''
        
        recvMsg, client = s_socket.recvfrom(1024)

        print('[UDP server id ' + str(self.id) + ']' +
                'received msg: ' + recvMsg.decode('utf-8'))
        if "response" in recvMsg:
            pass
        elif "request" in recvMsg:
            print(recvMsg.decode('utf-8'))
            sendMsg = "A ping response message was received from Peer " + \
                str(self.id)
            s_socket.sendto(sendMsg, client)
        '''
        
    def notifyDepart(self):
        print(f'Peer {self.id} will depart from the network.')
        
    def notifySucc(self):
        print(f'My first successor is now peer {self.next.id}')
        print(f'My second successor is not peer {self.next.id}') 
    
    
    def __str__(self):
        msg = f"[Peer {self.id}]"   
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
        if next is None:
            return None
        elif next is not None:
            return self._next._next
    
    @property
    def prev(self):
        return self._prev

    '''
    Setters
    '''
    
    @next.setter
    def next(self, successor):
        assert(isinstance(successor, Peer))
        self._next = successor
    
    @prev.setter
    def prev(self, predecessor):
        assert(isinstance(predecessor, Peer))
        self._prev = predecessor

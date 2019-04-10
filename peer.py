import socket

class Peer():

    def __init__(self, id, successor, predecessor):
        assert(type(id) is int and id>=0 and id<=255)
        assert(type(successor) is list)
        assert(type(predecessor) is int and predecessor>=0 and predecessor<=255)
        self._id = int(id)
        self._successor = successor
        self._predecessor = predecessor

    def sendPing(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(6.0) # set default timeout to 6 seconds
        sendMsg = "A ping request message was received from Peer " + self.id
        for s in [self.successor, self.successor.successor]:
            
            port = 50000 + s.id
            addr = ('localhost', port)

            client_socket.sendto(sendMsg, addr)

            try:
                data, serverAddr = client_socket.recvfrom(1024)
                print("ping to " + s.id + ', port: ' + port + ', with msg: ' + sendMsg)

            except socket.timeout:
                print(" <PACKET LOST> ping to " + s.id + ', port: ' + port)

            else:
                print("received from: " + server + ", data: " + data)
                
    def listenPing(parameter_list):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = 50000 + self.id
        server_socket.bind(('localhost', port))
        while True:
            recvMsg, clientAddr = server_socket.recvfrom(1024)
            print(recvMsg)
            if "response" in recvMsg:
                pass
            else if "request" in recvMsg:
                sendMsg = "A ping response message was received from Peer " + self.id
                server_socket.sendto(sendMsg, clientAddr)
        

    @property
    def id(self):
        return self._id

    @property
    def successor(self):
        return self._successor

    @property
    def predecessor(self):
        return self._predecessor

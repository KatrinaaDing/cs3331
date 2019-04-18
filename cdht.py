from peer import UDPListener, UDPSender, TCPHandler
import threading
import sys
import logging


FILE_REQUEST = 2
FILE_RESPONSE = 1

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
                
print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
currPeer = int(sys.argv[1])
succ = int(sys.argv[2])
nextSucc = int(sys.argv[3])
dropRate = sys.argv[5]

print('set up peer with id' + sys.argv[1])
UDPL = UDPListener(currPeer, succ, nextSucc, dropRate)
UDPS = UDPSender(currPeer, succ, nextSucc, dropRate)
TCPH = TCPHandler(currPeer, succ, nextSucc, dropRate)

UDPL.start()
UDPS.start()
TCPH.start()
print("PL is alive: " + str(UDPL.is_alive()))
print("pS is alive: " + str(UDPS.is_alive()))
print("tH is alive: " + str(TCPH.is_alive()))
while(True):
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
                nextPort = 50000+int(succ)
                print(f'preparing to send to {nextPort}')
                TCPheader = TCPH.TCPheader(FILE_REQUEST)
                msg = TCPheader + f' {file}'
                print(f'msg: f{msg}')
                TCPH.sendMsg(msg, nextPort)
                print(f'successfully send to port {nextPort}')
        else:
            print('try again')

'''
print("Enumerate: ")
for e in threading.enumerate():
    print(e)
'''



'''
class PeerList():
    
    def __init__(self):
        self._head = None
            
    # this base on a complete circular DHT structure
    def join(self, c, new):
        assert(isinstance(new, Peer))
        
        # request for expected succ and pred
        if (c.id < new.id and c.next.id > new.id) or (c.id < new.id and c.next.id < c.id):
            c.next.prev = new
            new.next = c.next
            c.next = new
            new.prev = c
            return (c, c.next)
        else:
            return self.join(c.next,new)
    
    def depart(self, leave):
        leave.notifyDepart()
        assert(isinstance(leave, Peer))
        leave.prev.next = leave.next
        leave.prev.notifySucc()
        leave.prev.prev.notifySucc()
     
    # for all peers, ping and check if aclive
    def pingAll(self):
        p = self.head
        while (p.id < p.next.id):
            p.sendPing()
            p = p.next
        p.sendPing()
    
    def UDPListenAll(self):
        p = self.head.next
        while (p.id < p.next.id):
            p.listenPing()
            p = p.next
        p.listenPing()
        
    # this base on a complete circular DHT structure 
    def __str__(self):
        msg = ""
        p = self.head
        while(p.id < p.next.id):
            msg += str(p) + '->' + str(p.next) + str(p.secNext) + '\n'
            p = p.next
        msg += str(p) + '->' + str(p.next) + str(p.secNext) + '\n' + 'Length: ' + str(self.length())
        return msg
    
    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, head):
        self._head = head


# test
pList = PeerList()
for p in [1, 3, 4, 5, 8, 10, 12, 15]:
    pList.insert(Peer(p))
    
print('------------Circular DHT-------------')
print(pList)
print('-------------------------------------')

's1' = threading.Thread(target=pList.UDPListenAll())
c = threading.Thread(target=pList.pingAll())

print("server treads start")
's1'.start()
print('client threads start')
c.start()


# t1.join() # join the pool and excute simutanously
# pirnt("server sockets all ready")
# t2.join() # will wait untill two threads done
# print("client send ping all finish")
'''

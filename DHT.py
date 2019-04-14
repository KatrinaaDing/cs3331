from peer import Peer
import threading
import sys

class PeerList():
    
    def __init__(self):
        self._head = None
        
    def length(self):
        count = 1
        p = self.head
        while(p.id < p.next.id):
            count += 1
            p = p.next
        return count
    
    # this is for initialisation of circular DHT structure
    def insert(self,new):
        # inserting the first peer
        if self.head is None:
            self.head = new
        # inserting the second peer
        elif self.head.next is None and self.head.prev is None:
           self.head.next = new
           self.head.prev = new
           new.next = self.head
           new.prev = self.head
        
        # inserting the third peer
        elif self.length() is 2:
            if new.id > self.head.id and new.id < self.head.next.id:
                new.prev = self.head
                new.next = self.head.next
                self.head.next = new
                new.next.prev = new
            
            elif new.id > self.head.id and new.id > self.head.next.id:
                new.next = self.head
                new.prev = self.head.prev
                self.head.prev = new
                new.prev.next = new
        
        else:
            self.join(self.head, new)
            
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

from peer import UDPListener, UDPSender, TCPHandler
import threading
import sys
import logging


FILE_REQUEST = 2
FILE_RESPONSE = 1
QUIT_NOTIFY = 3

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
id = int(sys.argv[1])
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
                
        elif flag == 'quit':
                TCPheader = TCPH.TCPheader(QUIT_NOTIFY)
                msg_to_prev = f'{TCPH.next} {TCPH.secNext}'
                prev_port = 50000+TCPH.prev
                msg_to_secPrev = f'{TCPH.prev} {TCPH.next}'
                secPrev_port = 50000+TCPH.secPrev
                
                msg = f'{TCPheader} {msg_to_prev} Peer {TCPH.id} will depart from the network.'
                TCPH.sendMsg(TCPheader, prev_port)
                msg = f'{TCPheader} {msg_to_secPrev} Peer {TCPH.id} will depart from the network.'
                TCPH.sendMsg(TCPheader, secPrev_port)
        else:
            print('try again')

'''
print("Enumerate: ")
for e in threading.enumerate():
    print(e)
'''


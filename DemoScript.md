## part 1

##### 7.1.1 show script
This is the sample set up script, and now I run my program, which is written in python3.

##### 7.1.2 Show UDP ping msg
My ping message is sent by UDP.
I have a thread named `pingSender`, this will send ping msg with `REQUEST` flag and a **unique seq number** every **20 seconds**. The format of ping msg is defined on the right hand side.

The helper function `sendPingMsg` is defined here, which send msg to a specific port from a random port. I'll reset this number after demo.

There is another thread named `pingListener`, the socket binds to a specific port to listen ping msg.

When it get a ping msg, it will firstly print out the msg. Then, if it's `REQUEST` ping, it send back the `RESPONSE` with same seq number. And if it's `RESPONSE` ping msg, it'll update the latest sequence number of this successors. I'll talk about this later.

##### 7.1.3 + 7.1.4 Show ping msg
So now let's go back to xterms. From the xterms you can see all peers are printing ping `REQUEST` from their predecessor, and ping `RESPONSE` from their successors. The peer id are correct.


## part 2

##### 7.2.1
Now I'm going to demonstrate part 2.

We have the file `2012.pdf` in the folder, and now let `Peer 8` reqeust 2012. 

##### 7.2.2
Once I enter that, the while loop, like input monitor, will catch it and validate the file name, if it's invalid it'll print error. If the file name is valid, it'll firstly send the `FILE_REQUEST` to itself to see if itself is the expected file holder, if not, it forward the `REQUEST` to it's first successors. You can see that `Peer 10`, `Peer 12` and `Peer 15` received this request and says that it doesn't have the file. And finally `Peer 1` receive the `FILE_REQUEST` and send `RESPONSE` directly to `Peer 8`. 

##### 7.3.3
The `FILE_REQUEST` and `FILE_RESPONSE` message are sent using TCP. The message is defined at the right hand side.

The helper function `sendTCPMsg` deal with that. It will creat a socket with **random** port, and try to connect to destination's socket. If the destination's socket is being used, it'll wait for 1 second and try to connect again. 
There's another thread called `TCPHandler`, which accept connection from other peers. 

After the file holder peer sending `FILE_RESPONSE` to the requesting peer, it'll start it's `FileHandler` thread.

When the requesting peer receive the `FILE_RESPONSE`, it and start it's `FileHandler` thread.


This is sent by the helper function `sendFileMsg`, it will send file segment from a random port to the destination port using UDP. It also take in the **drop probability**, which is accepted from command line. if the random float is less than the drop rate, the pkt is considered lost.

 As the destination port which listens for file segment is not specified in assignment spcification, so I make it this number to avoid concurrency. 

##### 7.3.4
Now let's go back to the folder and we can see the `received_file.pdf` is identical with `2012.pdf`. Also two log text files are written by requesting peer and responding peer seperately. 

##### 7.3.5
From the log file...

## part 3
For part 3, let us type 'quit' at `Peer 10`, then the `inputMonitor` will identify the `quit` flag and send TCP msg to its predecessors with `QUIT_NOTIFY` flag. 

When `Peer 8` and `Peer 5` receive this flag, they will print out the message and update their successors. After update, they will start ping to their new successors, and `Peer 12` and `Peer 15` will also update their predecessors according to the ping requests they received.

## part 4

Now let's kill `Peer 5`. Then `Peer 5` will no longer respond ping request. As I mention above, each peer will record the ping sequance number from it's successors' `RESPONSE`, if it finds that one of its successor have 4 seq number less than another one, it will think it's dead, and it will send `INFO_REQUEST` to the alive succssors for new successos information. Then it will balance the last received sequance number a little bit, so it give time for the destination peer send back `INFO_RESPONSE`.

This is sent over TCP by helper funcion `sendTCPMsg`.

When a peer get the `INFO_RESPONSE`, in order to send a correct successors information, it first check if the dead peer is still in its successors. For example, if `Peer 4` has not update its successors, it won't sent `INFO_RESPONSE` to `Peer 3`. 

After 2 more ping requests,  `Peer 3` finds that `Peer 5` is dead again, at this time, `Peer 4` has already update its successors information, so it can send back `INFO_RESPOSNE` with correct successors information to `Peer 3`. And `Peer 3` can update its successors now.

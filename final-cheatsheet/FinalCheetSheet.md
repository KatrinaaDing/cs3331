#### Intro
* network edge: clients, server
* network core: interconnected routers
* cable network: dedicated access to central office
* circuit switching: no sharing
	* FDM: share continuously
	* TDM: each one share whole bandwidth
	* #_Pic_#
	* timing: setup + transfer + teardown
* Pkt switching: store and forward
	* Statistical multiplexing: everyone using entire capacity
* delay: d<sub>proc</sub>+d<sub>queue</sub>+d<sub>trans</sub>+d<sub>prop</sub>
	* d<sub>proc</sub> = `len(pkt)/BW`
	* d<sub>queue</sub> = `#pkt*len(pkt)/BW`
	* d<sub>prop</sub> = `len(link)/speed`  
* layer
	* Application (message): SMTP, HTTP, FTP, skype
	* Transport (segment): TCP, UDP
	* Network (datagram): IP
	* Link (frame): Ethernet, 802.11, PPP
	* Physical: bits on wire
* layer's harm
	* duplicate lower level functionality
	* information hiding
	* header really big
	* layer violation (when can't resist or untrustful ends) 

#### App Layer
* within machine: IPC
* between machine: socket
* http: 80, email: 25, ssh: 22
* P2P
	* S not always on, peer directly communicate 
	* + self scalability, speed, reliability, geographically distribution
	* - dcentralized control (no shared memory, might conflict)
* protocol: open / proprietary专利的
	* email: SMTP - TCP
	* remote terminal access: Telnet - TCP
	* file transfer: FTP - TCP
	* streaming multimedia: HTTP/RTP - TCP/UDP 
	* Internet telephony: SIP/RTP/proprietary - TCP/UDP(main)
* URL: protocol://host-name[:port]/directory-path/resource
* HTTP: stateless, can use cache (proxy S)
	* 1.0: GET, POST, HEAD
	* 1.1: G/P/H, PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH
	* msg: ASCII  
	* status code: 200OK, 301Moved, 304 NotModified, 404NotFound, 505NotSupport
	* Wont send obj if cache has latest version
	* non-persistent HTTP have diff socket for each request
* HTTP Relication
	* spread load
	* content closer to C
	* - direct client to particular  relicas
	* - expensive
* HTTPs: encrypted by TLS
	* + Autentication
	* Bidirectional encription
* SMTP: mail, port 25, msg in 7-bit ASCII
	* SMTP: push, multipart msg
	* HTTP: pull, encapsulated in its own response msg 
	* persistent connection
	* Server-Client
	* POP: server not store msg
	* IMAP: server store msg
* DNS
	* root know all TLD (depth limit 128)
	* 1 zone has 1 authoritative DNS server
	* decentralized - doesn't scale
	* cache can expired (TTL)
* DNS resolution
	* iterative: load on local DNS server
	* recursive load on root server 
* DNS RRs (name, value, type, TTL)
	* A (hostname, IP)
	* CNAME (alias, canonical (real) name)
	* NS (domain, authoritative server's host name)
	* MX (name, name's mailserver's name)
* DNS msg
	* 16 bits identification
	* 16 bits flag
* Only within domain
	* Name could map to multiple IP
	* Multiple names for same IP
* DNS poisoning: send fake replies to DNS
* DASH
	* S: divides video to chunks, encoded at different rates, provide URLs for different chunks.
	* C: periodically measured S-C BW, requests one chunk at a time.
	* C determine: when to request, what encoding rate to request, where to request
* CDN
	* cachine and replication as a server
	* #_pic_#
* P2P 
	* C-S: D<sub>c-s</sub> >= max{NF/u<sub>s</sub>,F/d<sub>min</sub>}
	* P2P: D<sub>P2P</sub> >= max{F/u<sub>s</sub>,F/d<sub>min</sub>,NF/(u<sub>s</sub>+sum(u<sub>i</sub>))} 
	* rarest first
	* re-evaluate top 4 every 10s and random every 30s (optimistic unchoke)
* DHT (P2P database): infomation->num, put (key,value) in the peer closest to the key.


#### Transport Layer
* Executing within OS Kernal
* provide logical communication
* TCP
	 * point-to-point: one sender, one receiver
	* reliable, in-orfer byte steam
	* pipelined: congestion and flow ctrl
	* send and receive buffers
	* full duplex data: bi-directional data flow
	* connection-oriented: handshaking
	* flow ctrl: sender won't overwhelm receiver
		* rwnd + RcvBuffer(default 4096) = receiver side buffer
	* - timing, throughput guarantee, security
	* 4 tuple (srcIP; src Port; dest IP, dest Port)
	* 20 bytes header: srcPort, destPort, seq#, ACK#, len(header), flag, cwnd, checksum, urgent pointer
* UDP
	* unreliable transfer
	* - reliability, flow ctrl, congestion ctrl, timing, throughput guarantee, security, connection setup
	* 2 tuple (dest IP; dest Port)
	* out of order, connectionless
	* 8 bytes header: srcPort#, destPort#, len(payload+header), checksum, payload
	* app: DNS, DHCP, SNMP, RIP, game, voice/video chat
* Well-known port < 1024
* Reliable transfer
	* Checksums (error detection)
	* Timer (loss detection)
	* ACK (cumulative, selectiv)
	* Seq # (duplicate)
	* Sliding Window (efficiency) 
* rdt 2.0: ACK + NACK
* rdt 2.1: seq #
* rdt 2.2: NACK-free
* rdt 3.0: timer (Stop N Go)
	* detect dup
	* U<sub>sender</sub> = (len(pkt)/BW) / (RTT+(len(pkt)/BW))
	* #_pic_#
* Pipelining
	* U<sub>sender</sub> = pipe# * (len(pkt)/BW) / (RTT+(len(pkt)/BW))
	* #_pic_#
* Go-Back-N
	* receiver window size = 1
	* receiver only resp last received ACK (no buffer)
	* sender window size < 2^m (m = seq# bit field)
	* window slides forward up to ACK
	* resend all out-of-order pkt
* Selective repeat
	* sender window size < 2^m-1 
	* sender only resend the lost (buffer ACK)
	* receiver window size < 2^m-1 
	* receiver resp ACK to each recv pkt (buffer pkt)
* Seq #: SendBase (ISN) + len(payload)
* EstimatedRTT = `(1-α) * EstimatedRTT + α * SampleRTT`
* DevRTT = `(1-β) * DevRTT + β * |SampleRTT-EstimatedRTT|`
* TimeoutInterval = `EstimatedRTT + 4 * DevRTT`
* TCP generation
	* send ACK for all pkt within 500ms
	* sind single ACK for both in-order segments
	* fast retransmit: triple dup ACK - resend 
* TCP three-way handshake
	* SYN pkt lost: sender wait for SYN-ACK (default 3s), and retransimit
* SYN flooding: send lots of fake SYNs, waste server's time
* SYN cokkie: Only open connection state when ACK is back
* Congestion control
	* end-end: no explicit feedback from network
		* congestion inferred from end-system observed loss, delay 
		* responsibility by TCP
	* nework-assisted: router provide feedback
		* explicit rate for sender to send that
* TCP sending rate ≈ cwnd/RTT bytes/sec
* Sender-side window = min{CWND, RWND}
* max window size = `BW * RTT / len(pkt)` (1 window sent for 1 RTT)

#### Network Layer

* Data plane: local, per-router function; determines how datagram arriving on router input port is forwarded to router output port; forwarding function
* Control plane: netwrok-wide logic; determine how datagram is routed amoung routers; traditional routing algorithm & SDN
* Longest prefix matching: performed by TCAM
* Rule of thumb: average buffering = `RTT * link capacity / sqrt(tcp flows#)`
* #pic#
* HOL blocking: in input port
* Scheduling: FIFO, priority (classify pkt), Round Robin (1 from each class)
* IP pkt
	* 20 bytes header
		* 4-bit version
		* 3-bit len(header)
		* 8-bit TOS or DSCP: allow pkt to be treated differently
		* 16-bit Total Length (Bytes)
		* 16-bit identification
		* 3-bit flag
		* 13-bit fragment offset
		* 8-bit TTL
		* 8-bit protocol (TCP: 6, UDP: 17)
		* 16-bit checksum
		* 32-bit src IP
		* 32-bit dest IP
* Classful addressing: A: 0-8, B: 0-16, C: 0-24
* CIDR: arbitrary length. host part: all "1" for broadcast, all "0" is subnet address.
* DHCP (port: 67 at server, 68 at client) 
	* discover: host broadcast destIP=all"1"
	* offer: DHCP resp
	* request: host reqeust for IP
	* ACK: DHCP give IP (transaction ID smae as reqeust)
	* encapsulated in UDP: IP addr, len(lease), subnet mask, DNS server, default gateway
* ISP get block of addresses from ICANN, RIR act as intermediaries
* Private addr: 10.0.0.0/8, 172.16.0.0/12, 192,168.0.0/16
* NAT 
	* (src IP, port) -> (NAT IP, new port) 
	* 16-bit port# field
	* only process up to layer 3
	* violates end-to-end argument
	* requires recalculation of TCP and IP checksum
	* cannot manipulate TCP port
	* some IP and Port# is encrypted
	* has to be aware of change of port#
	* sol
		*  static map: A always map to B
		*  UPnP,IGD: learn public IP, add/rm port mapping
* Internet routing
	* intra-domain: AS, Link State (OSPF), DV (RIP) 
	* inter-domain: Path Vectoer (BGP)
* Link State (global)
	* flood LSA of each chagnes: keep copy locally
	* limited size
	* inconsistent: forwarding loop
	* oscilation: e.g. when cost = trafic loads...
* Distance Vector (decentralised): only to neighbour, scales
	
	
#### Link layer
* Focus on subnet
* service
	* framing, link access: encapsulate, MAC addr in frame header
	* reliable delievery between physically adjacent node
	* flow control
	* error detection
	* error correction
	* have-duplex and full-duplex
* Implemented in each host's adapter (NIC) or on a chip
* Attach into host's system buses
* MAC/LAN/physical/Ethernet address: 48 bits hexa, unique, portable (can be under any subnet), used to get pkt between interfaces on same networks
* ARP table: each node's IP/MAC addr, TTL
* ARP cache poisoning: eplies to an ARP query with fack MAC addr - need physical access to the network
* Ethernet: physical
	* bus: can collide - CSMA/CD 
	* star: active switch in center: no sharing, no CSMA/CD, can buffer
	* unrealiable, connectionless
* Ethernet frame structure
	* preamble序文: 7 bytes, sued to synchronize receiver, sender clock rates
	* address: 6 bytes src, dest MAC addr
	* type: indicate higher protocol (mostly IP)
	* CRC at receiver: error detected that frame is dropped
* Ethernet switch
	* active role: store, forward frames, examine incomming MAC addr  
	* transparent: hosts are unaware of presence of switches
	* self-learning/plug-and-play 
	* buffer pkt, can transmit simultaneously
* Switch Poisoning: attacker fills up switch table with fake MAC addr
* Wireless link
	* base station: e.g. cell tower, 802.11 AP 
	* backbone link
	* multiple access protocol coordinates link access
	* various data rates, transmission distance
	* handoff: mobile changes base station providing conneciton into wired network
	* characteristic
		* Hidden terminal problem (CS not working)
		* Signal attenuation衰减
* 802.11
	* AP admin chooses frequency for AP
	* host: must associate with an AP, will typically run DHCP to get IP in AP's subnet
	*  passive scanning: device receive AP's beacon信号
	*  active scanning: device broadcase beacon
	*  CSMA/CA
* Collision in 802.11
	* No concept of global collision
	* Collisions are at receiver, not sender
	* Goal: detectect if receiver can clearly hear sender, tell other sender to shut up
* CSMA/CA
	1. sender: if sense channel idle空闲 for DIFS then transmit entire fram
	2. sender: if sense channle busy: start random backoff time, timer counts down while channel idle, transmit when timer expires, if no ACK, increase random backoff interval, repeat
	3. receiver: if received OK: return ACK after SIFS
	
	* sender first ransmits small RTS
	* BS broadcasts CTS (including time) in response to RTS
	* - bandwidth: have to sent and wait for RTS each time before send a pkt


#### Multimedia
* Analog signal: continuous
	* telephone: 8000 sample/sec = 8000Hz
	* CD music: 44100 sample/sec
	* each sample quantized (rounded)
	* each quantized value represented by bits
	* receiver converts bits back to analog signal (quality reuction)
* Example rates
	* CD: 1.411 Mbps
	* MP3: 96128160 kbps
	* Internet telephony: 5.3 kbps and up
* Video
	* often segments to blocks (2-10 sec long) 
	* digital image = array of pixel
	* coding
		* spatial (within img): 2 val: color val, repeated #
		* tmporal (between img): send differences from frame i
* CBR: video encoding rate fixed
* VBR: video encoding rate chagnes as amount of spatial, temporal coding changes
* Application type
	* straming, stored audio, video
	* conversation voice/video over IP
	* streaming live audio/video 
* Solution to network delay
	*  playout delay
	*  client-side buffering

	
	
### Abbreviation

* ARQ (Automatic Repeat Request): an error-control method for data transmission that uses ACK.
* AIMD (Additive Increase Multiplicative Decrease)
* AS (Autonomous System): domain
* ARP (Address Resolution Protocol)
* AP (Access Point)

* BGP (Border Gateway Protocol)
* BBS (Basic Service Set)

* CDN (Content Distribution Networks)
* CBR (Constant Bit Rate): video encoding rate fixed
* CA (Congestion Avoidance)
* CIDR (Classless InterDomain Routing)
* CSMA (Carrier Sense Multiple Access)
* CS (Carrier Sense)
* CD (Collision Detect)
* CA (Collision Avoidance)
* CRC (Cyclic Redundancy Check)
* CTS (Clear to Send)
* CBR (Bonstant Bit Rate)

* DSL (Digital Subscriber Line)
* DNS (Domain Name System)
* DASH (Dynamic, Adaptive Streaming over HTTP)
* DHCP (Dynamic Host Configuration Protocol)
* DDoS (Distributed Denial of Server): flooding target with a constant flood of trafic.
* DSCP (Differentiated Services Code Point)
* DV (Distance Vector)
* DIFS (DCF Inter-Frame Space)

* FFTH (Fiber to the home)
* FIFO (First In First Out)

* HFC (Hybrid混合的 fiber coax)
* HOL (Head-of-the-Line)


* IPC (Interprocess communication):shared memory.
* ISP (Internet Serverce Provider)
* IMAP (Internet Mail Access Protocol)
* ISN (Initial Sequence Number)
* ICANN (Internet Corporation for Assigned Names and Numbers)
* IGD (Internet Gateway Device)

* LSA (Link State Advertisement)

* MTU (Maximum Segment Size)

* NAT (Network Address Translation)
* NIC (Network Interface Card)

* OSPF (Open Shortest Path First)

* POP (Post Office Protocol)
* P2P (Peer to Peer)
* PSH (Push Data Now): TCP flag, generally not used

* RDT (Reliable Data Transfer)
* RTP (Real Time Transfer)
* RR (Resources Record)
* RIP (Rrouting Information Protocol)
* RST (Reset)
* RIR (Regional Internet Registries)
* RTS (Request to Send)

* SMTP (Simple Mail Transfer Protocol)
* SNMP (Simple Network Management Protocol)
* SS (Slow Start)
* SDN (Software-difined Networking): centrlised (remote) servers
* SIFS (Shortest Interframe Spacing)

* TLS (Transport Layer Security)
* TLD (Top Level Domain)
* TCAM (Ternary Content Addressable Memories)
* TOS (Type of Service)

* URL (Uniform Resource Locator)
* URG (Urgent Data): TCP flag, generally not used.
* UPnP (Universal Plug and Play)

* VBR (Variable Bit Rate): video encoding rate chagnes as amount of spatial, temporal coding chagnes

* WWW (World Wide Web)



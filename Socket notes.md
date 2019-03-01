#Sockets
**Socket**, a way to speak to other programs using standard Unix file descriptors.  
**File descriptor**, an integer associated with an open file.
 
##Two Types of Internet Socket
### 1. **Stream Socket "`SOCK_STREAM`"**  
Arrive in order and is error-free.  
**Application**: Telnet, HTTP.   
Stream sockets use a protocol called "==TCP (The Transmission Control Prodocol==". TCP makes sure your data arrives sequentially and error-free.

**IP:** Internet Protocol, deals primarily with Internet routing and is not responsible for data integrity.

### 2. **Datagram Sockets "`SOCK_DGRAM`"**  
Also caleed connectionless.  
Arrive out of order and may drop one or two packet, but data within the arrived packet is error-free.  
**Application**: TFTP (trivial file transfer protocol), DHCPCD (a DHCP client), multiplayer games, streaming audio, video conferencing.  
Datagram sockets also use IP for routing, but **not using TCP**; they use "==UDP (User Datagram Protocol)==".  


## Low level Nonsense and Network Theory 

**Data Encapsulation**:   
_To send data_:  

1. A packet is born,  
2. the packet is wwrapped ("encapsulated") in a header (and rarely a footer) by the first protocol (e.g. TFTP),  
3. then the whole thing (TFTP header included) is encapsultated again by the next protocol (e.g. UDP),  
4. then again by the next (e.g. IP),=  
5. then again by the final protocol on the hardware (physical) layer (e.g. Ethernet).

_To receive data_:

1. The hardware strips the Ethernet header,
2. the kernel strips the IP and UDP headers, the TFTP program strips the TFTP header, 
3. and it finally has the data.

**Layered Network Model ("ISO/OSI")**:  

* Application
* Presentation
* Session
* Transport
* Network
* Data Link
* Physical

A layered model more _consistent with Unix_:

* Application Layer (*telnet, ftp, etc.*)
* Host-to-Host Transport Layer (*TCP, UDP*)
* Internet Layer (*IP and routing*)
* Network Access Layer (*Ethernet, wi-fi, or whatever*)

# IP Addresses, `struct`s, and Data Munging
IP Address, ports, sockets API, manipulates IP addresses.
##IP Addresses, versions 4 and 6
**The Internet Protocol Version 4 (IPv4)**, had addresses made up of four bytes, and was commonly written in "dots and number" form, e.g. `192.0.2.111`.  

Virtually every site on the Internet Uses IPv4.

However, 32-bit IPv4 address is not enough. Hence, IPv6 was born.

**IPv6**, a hexadecimal representation, with each two-byte chunk separated by a colon, e.g. `2001:0db8:c9d2:aee5:73e3:934a:a5ae:9551`.  
Generally there are lots of zeros in it, and you can compress them between two colons and leave off leading zeros for each byte pair. 

```
Each pair below are equivalent.

2001:0db8:c9d2:0012:0000:0000:0000:0051
2001:db8:c9d2:12::51

2001:0db8:ab00:0000:0000:0000:0000:0000
2001:db8:ab00::

0000:0000:0000:0000:0000:0000:0000:0001
::1
```
The address `::1` is the ==loopback address==. It always means "this machine I'm running on now". In IPv4, the loopback address is `127.0.0.1`.  

To represent an IPv4 address as and IPv6 addres, use following notation: 192.0.2.33 => `::ffff:192.0.2.33`.

## Port Numbers
Turns out that besides an IP address (used by the IP layer), there is another address that is used by TCP (stream sockets) and, coincidentally, by UDP (datagram sockets). It is a **16-bit number** that's like the local address for the connection, is used to tell computer (within a single IP address) which service is this data for.


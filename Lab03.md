# Lab03 by Katrina

## Exercise 2
### Q1.
UDP.  
`Protocol: UDP (17)`  

### Q2.
`Source Port: 3742`  
`Destination Port: 53`  

### Q3. 
`Destination: 128.238.29.22`  
No. The default local DNS server is `128.238.29.22`.  

### Q4. 
1 Question. `Questions: 1`  
Type A. `www.mit.edu: type A, class IN`  
No, the query message doesn't contain answer. `Answer RRs: 0`  

### Q5.
`Answers` stores the IP address corresponding to the input name; `Authoritative nameserver` stores other authorized name servers; `Additional record` stores the Type A (IP address) DNS of those name servers.  


## Exercise 3
### Q1. 
Type `A`. As type `A` stores the IP address for a name.  

```
z5211336@cs3331$ dig www.cecs.anu.edu.au A

; <<>> DiG 9.7.3 <<>> www.cecs.anu.edu.au A
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11833
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 3, ADDITIONAL: 6

;; QUESTION SECTION:
;www.cecs.anu.edu.au.		IN	A

;; ANSWER SECTION:
www.cecs.anu.edu.au.	1165	IN	CNAME	rproxy.cecs.anu.edu.au.
rproxy.cecs.anu.edu.au.	1165	IN	A	150.203.161.98

;; AUTHORITY SECTION:
cecs.anu.edu.au.	1152	IN	NS	ns4.cecs.anu.edu.au.
cecs.anu.edu.au.	1152	IN	NS	ns3.cecs.anu.edu.au.
cecs.anu.edu.au.	1152	IN	NS	ns2.cecs.anu.edu.au.

;; ADDITIONAL SECTION:
ns2.cecs.anu.edu.au.	3105	IN	A	150.203.161.36
ns2.cecs.anu.edu.au.	2263	IN	AAAA	2001:388:1034:2905::24
ns3.cecs.anu.edu.au.	2263	IN	A	150.203.161.50
ns3.cecs.anu.edu.au.	2263	IN	AAAA	2001:388:1034:2905::32
ns4.cecs.anu.edu.au.	1152	IN	A	150.203.161.38
ns4.cecs.anu.edu.au.	1152	IN	AAAA	2001:388:1034:2905::26

;; Query time: 0 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Tue Mar 12 21:52:11 2019
;; MSG SIZE  rcvd: 260
```  

### Q2.
The canonical name is `rproxy.cecs.anu.edu.au`. It's IP address is `150.203.161.98`.  
The alias is easier for people to memorize.

```
z5211336@cs3331$  dig www.cecs.anu.edu.au CNAME

; <<>> DiG 9.7.3 <<>> www.cecs.anu.edu.au CNAME
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48700
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 3, ADDITIONAL: 6

;; QUESTION SECTION:
;www.cecs.anu.edu.au.		IN	CNAME

;; ANSWER SECTION:
www.cecs.anu.edu.au.	1229	IN	CNAME	rproxy.cecs.anu.edu.au.

;; AUTHORITY SECTION:
cecs.anu.edu.au.	1216	IN	NS	ns4.cecs.anu.edu.au.
cecs.anu.edu.au.	1216	IN	NS	ns2.cecs.anu.edu.au.
cecs.anu.edu.au.	1216	IN	NS	ns3.cecs.anu.edu.au.

;; ADDITIONAL SECTION:
ns2.cecs.anu.edu.au.	3169	IN	A	150.203.161.36
ns2.cecs.anu.edu.au.	2327	IN	AAAA	2001:388:1034:2905::24
ns3.cecs.anu.edu.au.	2327	IN	A	150.203.161.50
ns3.cecs.anu.edu.au.	2327	IN	AAAA	2001:388:1034:2905::32
ns4.cecs.anu.edu.au.	1216	IN	A	150.203.161.38
ns4.cecs.anu.edu.au.	1216	IN	AAAA	2001:388:1034:2905::26

;; Query time: 0 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Tue Mar 12 21:51:07 2019
;; MSG SIZE  rcvd: 244 
```

### Q3.
The Authority Section displays the autority DNS servers for that domain (it may be contained in secondary zones).  
From the above example, the Authority Section has three name servers with Type `NS`.

The Additional Section displays those IPv4 addresses of the authoritive name servers in IPv6.  
From the above example, the Additional Section, the Type A records stores IPv4 address, and the Type AAAA records stores IPv6 address. Each pair of them corresponds to same name server.

### Q4. 
The IP address of the local nameserver is `127.0.0.1`.  

```
z5211336@drum15:~$ dig localhost

; <<>> DiG 9.7.3 <<>> localhost
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6086
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 1

;; QUESTION SECTION:
;localhost.			IN	A

;; ANSWER SECTION:
localhost.		63755	IN	A	127.0.0.1

;; AUTHORITY SECTION:
localhost.		63755	IN	NS	localhost.

;; ADDITIONAL SECTION:
localhost.		63755	IN	AAAA	::1

;; Query time: 0 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Thu Mar 14 18:58:21 2019
;; MSG SIZE  rcvd: 85
```



### Q5.
The name servers are `ns2.cecs.anu.edu.au`, `ns3.cecs.anu.edu.au`, `ns4.cecs.anu.edu.au`.  
Their corresponding IP addresses are `150.203.161.36`, `150.203.161.50`, `150.203.161.38`.  
Type `NS` is sent to achieve this information as it stores all authority DNS servers for that domain.  

```
z5211336@cs3331$ dig cecs.anu.edu.au NS

; <<>> DiG 9.7.3 <<>> cecs.anu.edu.au NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61371
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 6

;; QUESTION SECTION:
;cecs.anu.edu.au.		IN	NS

;; ANSWER SECTION:
cecs.anu.edu.au.	3349	IN	NS	ns3.cecs.anu.edu.au.
cecs.anu.edu.au.	3349	IN	NS	ns4.cecs.anu.edu.au.
cecs.anu.edu.au.	3349	IN	NS	ns2.cecs.anu.edu.au.

;; ADDITIONAL SECTION:
ns2.cecs.anu.edu.au.	1686	IN	A	150.203.161.36
ns2.cecs.anu.edu.au.	208	IN	AAAA	2001:388:1034:2905::24
ns3.cecs.anu.edu.au.	844	IN	A	150.203.161.50
ns3.cecs.anu.edu.au.	844	IN	AAAA	2001:388:1034:2905::32
ns4.cecs.anu.edu.au.	23697	IN	A	150.203.161.38
ns4.cecs.anu.edu.au.	3349	IN	AAAA	2001:388:1034:2905::26

;; Query time: 5 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Tue Mar 12 22:15:50 2019
;; MSG SIZE  rcvd: 219

```

### Q6. 
It's `engplws008.ad.unsw.edu.au.` and `engplws008.eng.unsw.edu.au.`. The type of DNS query is PTR, which maps an IP address to a hostname (like reverse Type A).  
 

```
z5211336@vx1:.../2/z5211336$ dig -x 149.171.158.109

; <<>> DiG 9.7.3 <<>> -x 149.171.158.109
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 35976
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 6, ADDITIONAL: 5

;; QUESTION SECTION:
;109.158.171.149.in-addr.arpa.	IN	PTR

;; ANSWER SECTION:
109.158.171.149.in-addr.arpa. 139 IN	PTR	engplws008.ad.unsw.edu.au.
109.158.171.149.in-addr.arpa. 139 IN	PTR	engplws008.eng.unsw.edu.au.

;; AUTHORITY SECTION:
in-addr.arpa.		31603	IN	NS	f.in-addr-servers.arpa.
in-addr.arpa.		31603	IN	NS	d.in-addr-servers.arpa.
in-addr.arpa.		31603	IN	NS	e.in-addr-servers.arpa.
in-addr.arpa.		31603	IN	NS	b.in-addr-servers.arpa.
in-addr.arpa.		31603	IN	NS	a.in-addr-servers.arpa.
in-addr.arpa.		31603	IN	NS	c.in-addr-servers.arpa.

;; ADDITIONAL SECTION:
a.in-addr-servers.arpa.	36444	IN	A	199.180.182.53
c.in-addr-servers.arpa.	49412	IN	A	196.216.169.10
d.in-addr-servers.arpa.	80013	IN	A	200.10.60.53
e.in-addr-servers.arpa.	71996	IN	A	203.119.86.101
f.in-addr-servers.arpa.	5387	IN	A	193.0.9.1

;; Query time: 0 msec
;; SERVER: 129.94.242.45#53(129.94.242.45)
;; WHEN: Thu Mar 14 14:30:05 2019
;; MSG SIZE  rcvd: 306
```


### Q7.   
No, as the flags don't contain `AA` flag, which means it's not the authoritative answer.

```
z5211336@vx1:.../2/z5211336$ dig @129.94.242.33 yahoo.com MX

; <<>> DiG 9.7.3 <<>> @129.94.242.33 yahoo.com MX
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 35258
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 8

;; QUESTION SECTION:
;yahoo.com.			IN	MX

;; ANSWER SECTION:
yahoo.com.		159	IN	MX	1 mta5.am0.yahoodns.net.
yahoo.com.		159	IN	MX	1 mta6.am0.yahoodns.net.
yahoo.com.		159	IN	MX	1 mta7.am0.yahoodns.net.

;; AUTHORITY SECTION:
yahoo.com.		67943	IN	NS	ns2.yahoo.com.
yahoo.com.		67943	IN	NS	ns1.yahoo.com.
yahoo.com.		67943	IN	NS	ns3.yahoo.com.
yahoo.com.		67943	IN	NS	ns4.yahoo.com.
yahoo.com.		67943	IN	NS	ns5.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		451657	IN	A	68.180.131.16
ns1.yahoo.com.		14049	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		461546	IN	A	68.142.255.16
ns2.yahoo.com.		1394	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		71802	IN	A	203.84.221.53
ns3.yahoo.com.		72496	IN	AAAA	2406:8600:b8:fe03::1003
ns4.yahoo.com.		290158	IN	A	98.138.11.157
ns5.yahoo.com.		354473	IN	A	119.160.253.83

;; Query time: 0 msec
;; SERVER: 129.94.242.33#53(129.94.242.33)
;; WHEN: Thu Mar 14 14:05:41 2019
;; MSG SIZE  rcvd: 360
```

### Q8.
It doesn't have answer and the status is `REFUSED` (recursive query denided. Also, flags in header only has `qr` and `rd` but not `ra` (recursive available).  

```
z5211336@vx1:.../2/z5211336$ dig @150.203.161.36 yahoo.com MX

; <<>> DiG 9.7.3 <<>> @150.203.161.36 yahoo.com MX
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: REFUSED, id: 21564
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;yahoo.com.			IN	MX

;; Query time: 8 msec
;; SERVER: 150.203.161.36#53(150.203.161.36)
;; WHEN: Thu Mar 14 14:44:57 2019
;; MSG SIZE  rcvd: 27
```

### Q9. 
`MX` is sent.

```
z5211336@drum15:~$ dig @ns2.yahoo.com. yahoo.com MX

; <<>> DiG 9.7.3 <<>> @ns2.yahoo.com. yahoo.com MX
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29803
;; flags: qr aa rd; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 8
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;yahoo.com.			IN	MX

;; ANSWER SECTION:
yahoo.com.		1800	IN	MX	1 mta6.am0.yahoodns.net.
yahoo.com.		1800	IN	MX	1 mta7.am0.yahoodns.net.
yahoo.com.		1800	IN	MX	1 mta5.am0.yahoodns.net.

;; AUTHORITY SECTION:
yahoo.com.		172800	IN	NS	ns1.yahoo.com.
yahoo.com.		172800	IN	NS	ns3.yahoo.com.
yahoo.com.		172800	IN	NS	ns2.yahoo.com.
yahoo.com.		172800	IN	NS	ns5.yahoo.com.
yahoo.com.		172800	IN	NS	ns4.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		1209600	IN	A	68.180.131.16
ns2.yahoo.com.		1209600	IN	A	68.142.255.16
ns3.yahoo.com.		1209600	IN	A	203.84.221.53
ns4.yahoo.com.		1209600	IN	A	98.138.11.157
ns5.yahoo.com.		1209600	IN	A	119.160.253.83
ns1.yahoo.com.		86400	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		86400	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		86400	IN	AAAA	2406:8600:b8:fe03::1003

;; Query time: 149 msec
;; SERVER: 68.142.255.16#53(68.142.255.16)
;; WHEN: Thu Mar 14 19:38:06 2019
;; MSG SIZE  rcvd: 360
```

### Q10.
6 DNS servers I have to query. And my IP address is `129.94.210.20`.  


1. for `.` (NS)
2. for `au.` (NS)
3. for `edu.au.` (NS)
4. for `unsw.edu.au` (NS)
5. for `cse.unsw.edu.au` (NS)
6. for `lyre00.cse.unsw.edu.au` (A)  

```
z5211336@drum15:~$ dig . NS

; <<>> DiG 9.7.3 <<>> . NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 61312
;; flags: qr rd ra; QUERY: 1, ANSWER: 13, AUTHORITY: 0, ADDITIONAL: 13

;; QUESTION SECTION:
;.				IN	NS

;; ANSWER SECTION:
.			47606	IN	NS	i.root-servers.net.
.			47606	IN	NS	j.root-servers.net.
.			47606	IN	NS	k.root-servers.net.
.			47606	IN	NS	l.root-servers.net.
.			47606	IN	NS	a.root-servers.net.
.			47606	IN	NS	h.root-servers.net.
.			47606	IN	NS	g.root-servers.net.
.			47606	IN	NS	c.root-servers.net.
.			47606	IN	NS	m.root-servers.net.
.			47606	IN	NS	e.root-servers.net.
.			47606	IN	NS	b.root-servers.net.
.			47606	IN	NS	d.root-servers.net.
.			47606	IN	NS	f.root-servers.net.

;; ADDITIONAL SECTION:
a.root-servers.net.	316144	IN	A	198.41.0.4
a.root-servers.net.	332855	IN	AAAA	2001:503:ba3e::2:30
b.root-servers.net.	494471	IN	A	199.9.14.201
b.root-servers.net.	54885	IN	AAAA	2001:500:200::b
c.root-servers.net.	449353	IN	A	192.33.4.12
c.root-servers.net.	17353	IN	AAAA	2001:500:2::c
d.root-servers.net.	207631	IN	A	199.7.91.13
d.root-servers.net.	240200	IN	AAAA	2001:500:2d::d
e.root-servers.net.	318516	IN	A	192.203.230.10
e.root-servers.net.	65912	IN	AAAA	2001:500:a8::e
f.root-servers.net.	54885	IN	A	192.5.5.241
f.root-servers.net.	17353	IN	AAAA	2001:500:2f::f
g.root-servers.net.	326603	IN	A	192.112.36.4

;; Query time: 1 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Thu Mar 14 18:24:53 2019
;; MSG SIZE  rcvd: 508

z5211336@drum15:~$ dig @i.root-servers.net. au. NS

; <<>> DiG 9.7.3 <<>> @i.root-servers.net. au. NS
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 50189
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 10, ADDITIONAL: 15
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;au.				IN	NS

;; AUTHORITY SECTION:
au.			172800	IN	NS	a.au.
au.			172800	IN	NS	r.au.
au.			172800	IN	NS	v.au.
au.			172800	IN	NS	u.au.
au.			172800	IN	NS	q.au.
au.			172800	IN	NS	b.au.
au.			172800	IN	NS	d.au.
au.			172800	IN	NS	t.au.
au.			172800	IN	NS	c.au.
au.			172800	IN	NS	s.au.

;; ADDITIONAL SECTION:
a.au.			172800	IN	A	58.65.254.73
a.au.			172800	IN	AAAA	2407:6e00:254:306::73
b.au.			172800	IN	A	58.65.253.73
b.au.			172800	IN	AAAA	2407:6e00:253:306::73
c.au.			172800	IN	A	162.159.24.179
c.au.			172800	IN	AAAA	2400:cb00:2049:1::a29f:18b3
d.au.			172800	IN	A	162.159.25.38
d.au.			172800	IN	AAAA	2400:cb00:2049:1::a29f:1926
q.au.			172800	IN	A	65.22.196.1
q.au.			172800	IN	AAAA	2a01:8840:be::1
r.au.			172800	IN	A	65.22.197.1
r.au.			172800	IN	AAAA	2a01:8840:bf::1
s.au.			172800	IN	A	65.22.198.1
s.au.			172800	IN	AAAA	2a01:8840:c0::1
t.au.			172800	IN	A	65.22.199.1

;; Query time: 47 msec
;; SERVER: 192.36.148.17#53(192.36.148.17)
;; WHEN: Thu Mar 14 18:25:21 2019
;; MSG SIZE  rcvd: 504

z5211336@drum15:~$ code WebServer.py
z5211336@drum15:~$ code WebServer.py
z5211336@drum15:~$ 
z5211336@drum15:~$ 
z5211336@drum15:~$ 
z5211336@drum15:~$ 
z5211336@drum15:~$ dig @a.au. edu.au NS

; <<>> DiG 9.7.3 <<>> @a.au. edu.au NS
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63768
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 4, ADDITIONAL: 8
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;edu.au.				IN	NS

;; AUTHORITY SECTION:
edu.au.			86400	IN	NS	q.au.
edu.au.			86400	IN	NS	t.au.
edu.au.			86400	IN	NS	s.au.
edu.au.			86400	IN	NS	r.au.

;; ADDITIONAL SECTION:
q.au.			86400	IN	A	65.22.196.1
r.au.			86400	IN	A	65.22.197.1
s.au.			86400	IN	A	65.22.198.1
t.au.			86400	IN	A	65.22.199.1
q.au.			86400	IN	AAAA	2a01:8840:be::1
r.au.			86400	IN	AAAA	2a01:8840:bf::1
s.au.			86400	IN	AAAA	2a01:8840:c0::1
t.au.			86400	IN	AAAA	2a01:8840:c1::1

;; Query time: 154 msec
;; SERVER: 58.65.254.73#53(58.65.254.73)
;; WHEN: Thu Mar 14 19:06:29 2019
;; MSG SIZE  rcvd: 264

z5211336@drum15:~$ dig @q.au. unsw.edu.au NS

; <<>> DiG 9.7.3 <<>> @q.au. unsw.edu.au NS
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 22054
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 3, ADDITIONAL: 5
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;unsw.edu.au.			IN	NS

;; AUTHORITY SECTION:
unsw.edu.au.		900	IN	NS	ns2.unsw.edu.au.
unsw.edu.au.		900	IN	NS	ns3.unsw.edu.au.
unsw.edu.au.		900	IN	NS	ns1.unsw.edu.au.

;; ADDITIONAL SECTION:
ns1.unsw.edu.au.	900	IN	A	129.94.0.192
ns2.unsw.edu.au.	900	IN	A	129.94.0.193
ns3.unsw.edu.au.	900	IN	A	192.155.82.178
ns1.unsw.edu.au.	900	IN	AAAA	2001:388:c:35::1
ns2.unsw.edu.au.	900	IN	AAAA	2001:388:c:35::2

;; Query time: 7 msec
;; SERVER: 65.22.196.1#53(65.22.196.1)
;; WHEN: Thu Mar 14 19:06:41 2019
;; MSG SIZE  rcvd: 187

z5211336@drum15:~$ dig @ns2.unsw.edu.au. cse.unsw.edu.au NS

; <<>> DiG 9.7.3 <<>> @ns2.unsw.edu.au. cse.unsw.edu.au NS
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 27873
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 2, ADDITIONAL: 4
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;cse.unsw.edu.au.		IN	NS

;; AUTHORITY SECTION:
cse.unsw.edu.au.	10800	IN	NS	beethoven.orchestra.cse.unsw.edu.au.
cse.unsw.edu.au.	10800	IN	NS	maestro.orchestra.cse.unsw.edu.au.

;; ADDITIONAL SECTION:
beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.172.11
beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.208.3
beethoven.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.242.2
maestro.orchestra.cse.unsw.edu.au. 10800 IN A	129.94.242.33

;; Query time: 4 msec
;; SERVER: 129.94.0.193#53(129.94.0.193)
;; WHEN: Thu Mar 14 19:06:55 2019
;; MSG SIZE  rcvd: 153

z5211336@drum15:~$ dig @beethoven.orchestra.cse.unsw.edu.au. lyre00.cse.unsw.edu.au A

; <<>> DiG 9.7.3 <<>> @beethoven.orchestra.cse.unsw.edu.au. lyre00.cse.unsw.edu.au A
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28478
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 2

;; QUESTION SECTION:
;lyre00.cse.unsw.edu.au.		IN	A

;; ANSWER SECTION:
lyre00.cse.unsw.edu.au.	3600	IN	A	129.94.210.20

;; AUTHORITY SECTION:
cse.unsw.edu.au.	3600	IN	NS	maestro.orchestra.cse.unsw.edu.au.
cse.unsw.edu.au.	3600	IN	NS	beethoven.orchestra.cse.unsw.edu.au.

;; ADDITIONAL SECTION:
maestro.orchestra.cse.unsw.edu.au. 3600	IN A	129.94.242.33
beethoven.orchestra.cse.unsw.edu.au. 3600 IN A	129.94.208.3

;; Query time: 0 msec
;; SERVER: 129.94.208.3#53(129.94.208.3)
;; WHEN: Thu Mar 14 19:07:17 2019
;; MSG SIZE  rcvd: 144
```



### Q11.
One physical machine CAN have serval names (e.g. alias) but ONLY ONE IP addresses  is associated with it.

## Exercise 4






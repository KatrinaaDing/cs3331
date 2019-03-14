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
### *Giving out the reason*

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
At the end of `dig` result, it's `129.94.208.3`.  

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
z5211336@vx1:.../2/z5211336$ dig yahoo.com MX

; <<>> DiG 9.7.3 <<>> yahoo.com MX
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54748
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 8

;; QUESTION SECTION:
;yahoo.com.			IN	MX

;; ANSWER SECTION:
yahoo.com.		238	IN	MX	1 mta5.am0.yahoodns.net.
yahoo.com.		238	IN	MX	1 mta6.am0.yahoodns.net.
yahoo.com.		238	IN	MX	1 mta7.am0.yahoodns.net.

;; AUTHORITY SECTION:
yahoo.com.		65117	IN	NS	ns4.yahoo.com.
yahoo.com.		65117	IN	NS	ns2.yahoo.com.
yahoo.com.		65117	IN	NS	ns5.yahoo.com.
yahoo.com.		65117	IN	NS	ns3.yahoo.com.
yahoo.com.		65117	IN	NS	ns1.yahoo.com.

;; ADDITIONAL SECTION:
ns1.yahoo.com.		347687	IN	A	68.180.131.16
ns1.yahoo.com.		11223	IN	AAAA	2001:4998:130::1001
ns2.yahoo.com.		351646	IN	A	68.142.255.16
ns2.yahoo.com.		111338	IN	AAAA	2001:4998:140::1002
ns3.yahoo.com.		68976	IN	A	203.84.221.53
ns3.yahoo.com.		7758	IN	AAAA	2406:8600:b8:fe03::1003
ns4.yahoo.com.		83190	IN	A	98.138.11.157
ns5.yahoo.com.		428812	IN	A	119.160.253.83

;; Query time: 6 msec
;; SERVER: 129.94.242.45#53(129.94.242.45)
;; WHEN: Thu Mar 14 14:52:47 2019
;; MSG SIZE  rcvd: 360
```

### Q10.
6 DNS servers I have to query.  

1. for `.` (NS)
2. for `au.` (NS)
3. for `edu.au.` (NS)
4. for `unsw.edu.au` (NS)
5. for `cse.unsw.edu.au` (NS)
6. for `lyre00.cse.unsw.edu.au` (A)  


### Q11.
Yes, e.g. virtual machine.  

## Exercise 4






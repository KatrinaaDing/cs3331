# Lab03 by Katrina

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

### Q3. *What is it mean by "make of"?*
The Authority Section displays the autority DNS servers for that domain (it may be contained in secondary zones).  
The Additional Section displays those IPv4 addresses of the authoritive name servers in IPv6.  

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




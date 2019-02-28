# COMP3331 Lab101



## Exercise 1
### 1.
Google's IP address: 172.217.25.164
### 2. 
name = localhost.
This IP address is the local computer's IP address.

## Exercise 2
 * `www.cse.unsw.edu.au` Yes
 * `www.getfittest.com.au` No
 * `www.mit.edu` Yes
 * `www.intel.com.au` Yes
 * `www.tpg.com.au` Yes
 * `www.hola.hp` No
 * `www.amazon.com` Yes
 * `www.tsinghua.edu.cn` Yes
 * `www.kremlin.ru` No
 * `8.8.8.8` Yes

`www.getfittest.com.au` and `www.hola.hp` are not valid hosts and are not reachable from Web browser. `www.kremlin.ru` can be transmitted packets using ping, but 0 packets received; however, it can be reachable by Web browser. ==Possible reason:== Government website has firewall that blocks ping request.

## Exercise 3
### 1.
There are 22 routers.  
There are 4 routers are part of the UNSW network (1, 3, 4, 5).  
Crossing the Pacific Ocean is between route 7 (`113.197.15.149`) and route 8 (`113.197.15.99`).  


Traceroot result:

```
wagner % traceroute www.columbia.edu
traceroute to www.columbia.edu (128.59.105.24), 30 hops max, 60 byte packets
 1  cserouter1-server.cse.unsw.EDU.AU (129.94.242.251)  0.118 ms  0.141 ms  0.126 ms
 2  129.94.39.17 (129.94.39.17)  1.152 ms  1.118 ms  1.095 ms
 3  libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  3.564 ms ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.937 ms  1.830 ms
 4  libcr1-po-5.gw.unsw.edu.au (149.171.255.165)  1.296 ms ombcr1-po-5.gw.unsw.edu.au (149.171.255.197)  1.278 ms  1.278 ms
 5  unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.294 ms unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.356 ms unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.305 ms
 6  138.44.5.0 (138.44.5.0)  1.650 ms  1.414 ms  1.436 ms
 7  et-1-3-0.pe1.sxt.bkvl.nsw.aarnet.net.au (113.197.15.149)  4.159 ms  2.469 ms  2.367 ms
 8  et-0-0-0.pe1.a.hnl.aarnet.net.au (113.197.15.99)  95.732 ms  95.360 ms  95.285 ms
 9  et-2-1-0.bdr1.a.sea.aarnet.net.au (113.197.15.201)  146.750 ms  146.805 ms  146.777 ms
10  abilene-1-lo-jmb-706.sttlwa.pacificwave.net (207.231.240.8)  146.760 ms  146.875 ms  146.848 ms
11  et-4-0-0.4079.rtsw.miss2.net.internet2.edu (162.252.70.0)  157.711 ms  157.702 ms  157.817 ms
12  et-4-0-0.4079.rtsw.minn.net.internet2.edu (162.252.70.58)  180.692 ms  180.763 ms  180.829 ms
13  et-1-1-5.4079.rtsw.eqch.net.internet2.edu (162.252.70.106)  229.391 ms  188.866 ms  202.591 ms
14  162.252.70.163 (162.252.70.163)  192.517 ms  188.783 ms  188.774 ms
15  ae-1.4079.rtsw.clev.net.internet2.edu (162.252.70.130)  197.227 ms  197.198 ms  197.159 ms
16  buf-9208-I2-CLEV.nysernet.net (199.109.11.33)  201.526 ms  201.539 ms  201.530 ms
17  syr-9208-buf-9208.nysernet.net (199.109.7.193)  204.785 ms  204.861 ms  204.755 ms
18  nyc-9208-syr-9208.nysernet.net (199.109.7.162)  210.386 ms  210.447 ms  210.432 ms
19  columbia.nyc-9208.nysernet.net (199.109.4.14)  210.521 ms  210.428 ms  210.411 ms
20  cc-core-1-x-nyser32-gw-1.net.columbia.edu (128.59.255.5)  210.590 ms  210.710 ms  210.855 ms
21  cc-conc-1-x-cc-core-1.net.columbia.edu (128.59.255.210)  211.640 ms  211.276 ms  211.191 ms
22  www.neurotheory.columbia.edu (128.59.105.24)  211.014 ms  210.986 ms  211.015 ms
```

Ping result:

```
wagner % ping 113.197.15.99
PING 113.197.15.99 (113.197.15.99) 56(84) bytes of data.
64 bytes from 113.197.15.99: icmp_req=1 ttl=57 time=94.8 ms
64 bytes from 113.197.15.99: icmp_req=2 ttl=57 time=94.9 ms
64 bytes from 113.197.15.99: icmp_req=3 ttl=57 time=94.9 ms
64 bytes from 113.197.15.99: icmp_req=4 ttl=57 time=95.0 ms
64 bytes from 113.197.15.99: icmp_req=5 ttl=57 time=94.9 ms
64 bytes from 113.197.15.99: icmp_req=6 ttl=57 time=95.0 ms
64 bytes from 113.197.15.99: icmp_req=7 ttl=57 time=95.0 ms
64 bytes from 113.197.15.99: icmp_req=8 ttl=57 time=95.1 ms
64 bytes from 113.197.15.99: icmp_req=9 ttl=57 time=94.9 ms
64 bytes from 113.197.15.99: icmp_req=10 ttl=57 time=94.9 ms
^C
--- 113.197.15.99 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9012ms
rtt min/avg/max/mdev = 94.889/94.976/95.136/0.419 ms
wagner % ping 113.197.15.149
PING 113.197.15.149 (113.197.15.149) 56(84) bytes of data.
64 bytes from 113.197.15.149: icmp_req=1 ttl=58 time=2.03 ms
64 bytes from 113.197.15.149: icmp_req=2 ttl=58 time=1.93 ms
64 bytes from 113.197.15.149: icmp_req=3 ttl=58 time=1.89 ms
64 bytes from 113.197.15.149: icmp_req=4 ttl=58 time=1.93 ms
64 bytes from 113.197.15.149: icmp_req=5 ttl=58 time=1.84 ms
64 bytes from 113.197.15.149: icmp_req=6 ttl=58 time=1.80 ms
64 bytes from 113.197.15.149: icmp_req=7 ttl=58 time=2.17 ms
64 bytes from 113.197.15.149: icmp_req=8 ttl=58 time=1.82 ms
64 bytes from 113.197.15.149: icmp_req=9 ttl=58 time=2.04 ms
64 bytes from 113.197.15.149: icmp_req=10 ttl=58 time=2.18 ms
^C
--- 113.197.15.149 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9014ms
rtt min/avg/max/mdev = 1.809/1.967/2.182/0.139 ms
```

### 2.
These three paths diverge at `138.44.5.0`. The organizaion of this router is Asia Pacific Network Information Centre (APNIC), and the router locates in Qeensland, which makes sense that those three paths diverge here.
==the third question How?===


```
wagner % whois 138.44.5.0

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2019, American Registry for Internet Numbers, Ltd.
#


NetRange:       138.44.0.0 - 138.44.255.255
CIDR:           138.44.0.0/16
NetName:        APNIC-ERX-138-44-0-0
NetHandle:      NET-138-44-0-0-1
Parent:         NET138 (NET-138-0-0-0-0)
NetType:        Early Registrations, Transferred to APNIC
OriginAS:
Organization:   Asia Pacific Network Information Centre (APNIC)
RegDate:        2003-12-11
Updated:        2009-10-08
Comment:        This IP address range is not registered in the ARIN database.
Comment:        This range was transferred to the APNIC Whois Database as
Comment:        part of the ERX (Early Registration Transfer) project.
Comment:        For details, refer to the APNIC Whois Database via
Comment:        WHOIS.APNIC.NET or http://wq.apnic.net/apnic-bin/whois.pl
Comment:
Comment:        ** IMPORTANT NOTE: APNIC is the Regional Internet Registry
Comment:        for the Asia Pacific region.  APNIC does not operate networks
Comment:        using this IP address range and is not able to investigate
Comment:        spam or abuse reports relating to these addresses.  For more
Comment:        help, refer to http://www.apnic.net/apnic-info/whois_search2/abuse-and-spamming
Ref:            https://rdap.arin.net/registry/ip/138.44.0.0

ResourceLink:  http://wq.apnic.net/whois-search/static/search.html
ResourceLink:  whois.apnic.net


OrgName:        Asia Pacific Network Information Centre
OrgId:          APNIC
Address:        PO Box 3646
City:           South Brisbane
StateProv:      QLD
PostalCode:     4101
Country:        AU
RegDate:
Updated:        2012-01-24
Ref:            https://rdap.arin.net/registry/entity/APNIC

ReferralServer:  whois://whois.apnic.net
ResourceLink:  http://wq.apnic.net/whois-search/static/search.html

OrgTechHandle: AWC12-ARIN
OrgTechName:   APNIC Whois Contact
OrgTechPhone:  +61 7 3858 3188
OrgTechEmail:  search-apnic-not-arin@apnic.net
OrgTechRef:    https://rdap.arin.net/registry/entity/AWC12-ARIN

OrgAbuseHandle: AWC12-ARIN
OrgAbuseName:   APNIC Whois Contact
OrgAbusePhone:  +61 7 3858 3188
OrgAbuseEmail:  search-apnic-not-arin@apnic.net
OrgAbuseRef:    https://rdap.arin.net/registry/entity/AWC12-ARIN


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2019, American Registry for Internet Numbers, Ltd.
#



Found a referral to whois.apnic.net.

% [whois.apnic.net]
% Whois data copyright terms    http://www.apnic.net/db/dbcopyright.html

% Information related to '138.44.0.0 - 138.44.255.255'

% Abuse contact for '138.44.0.0 - 138.44.255.255' is 'abuse@aarnet.edu.au'

inetnum:        138.44.0.0 - 138.44.255.255
netname:        AARNET
descr:          Australian Academic and Research Network
descr:          Building 9
descr:          Banks Street
country:        AU
org:            ORG-AAAR1-AP
admin-c:        SM6-AP
tech-c:         ANOC-AP
notify:         irrcontact@aarnet.edu.au
mnt-by:         APNIC-HM
mnt-lower:      MAINT-AARNET-AP
mnt-routes:     MAINT-AARNET-AP
mnt-irt:        IRT-AARNET-AU
status:         ALLOCATED PORTABLE
remarks:        -+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+
remarks:        This object can only be updated by APNIC hostmasters.
remarks:        To update this object, please contact APNIC
remarks:        hostmasters and include your organisation's account
remarks:        name in the subject line.
remarks:        -+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+
last-modified:  2017-10-09T13:02:43Z
source:         APNIC

irt:            IRT-AARNET-AU
address:        AARNet Pty Ltd
address:        26 Dick Perry Avenue
address:        Kensington, Western Australia
address:        Australia
e-mail:         abuse@aarnet.edu.au
abuse-mailbox:  abuse@aarnet.edu.au
admin-c:        SM6-AP
tech-c:         ANOC-AP
auth:           # Filtered
mnt-by:         MAINT-AARNET-AP
last-modified:  2010-11-08T08:02:43Z
source:         APNIC

organisation:   ORG-AAAR1-AP
org-name:       Australian Academic and Research Network
country:        AU
address:        Building 9
address:        Banks Street
phone:          +61-2-6222-3530
fax-no:         +61-2-6222-3535
e-mail:         irrcontact@aarnet.edu.au
mnt-ref:        APNIC-HM
mnt-by:         APNIC-HM
last-modified:  2017-10-09T12:56:36Z
source:         APNIC

role:           AARNet Network Operations Centre
remarks:
address:        AARNet Pty Ltd
address:        GPO Box 1559
address:        Canberra
address:        ACT  2601
country:        AU
phone:          +61 1300 275 662
phone:          +61 2 6222 3555
remarks:
e-mail:         noc@aarnet.edu.au
remarks:
remarks:        Send abuse reports to abuse@aarnet.edu.au
remarks:        Please include timestamps and offset to UTC in logs
remarks:        Peering requests to peering@aarnet.edu.au
remarks:
admin-c:        SM6-AP
tech-c:         BM-AP
nic-hdl:        ANOC-AP
mnt-by:         MAINT-AARNET-AP
last-modified:  2010-06-30T13:16:48Z
source:         APNIC

person:         Steve Maddocks
remarks:        Director Operations
address:        AARNet Pty Ltd
address:        26 Dick Perry Avenue
address:        Kensington
address:        Perth
address:        WA  6151
country:        AU
phone:          +61-8-9289-2210
fax-no:         +61-2-6222-7509
e-mail:         steve.maddocks@aarnet.edu.au
nic-hdl:        SM6-AP
mnt-by:         MAINT-AARNET-AP
last-modified:  2011-02-01T08:37:06Z
source:         APNIC

% This query was served by the APNIC Whois Service version 1.88.15-46 (WHOIS-NODE1)
```

### 3.

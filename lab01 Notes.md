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

`www.getfittest.com.au` and `www.hola.hp` are not valid hosts and are not reachable from Web browser. `www.kremlin.ru` can be transmitted packets using ping, but 0 packets received; however, it can be reachable by Web browser. Government website has firewall that blocks ping request for security reason.

## Exercise 3
### 1.
There are 22 routers.  
There are 4 routers are part of the UNSW network (1, 3, 4, 5).  
Crossing the Pacific Ocean is between route 7 (`113.197.15.149`) and route 8 (`113.197.15.99`) because the time is significantly different.


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
These three paths diverge at `138.44.5.0`. The organizaion of this router is Asia Pacific Network Information Centre (APNIC), and the router locates in Qeensland, which makes sense that those three paths diverge here. No, the number of hops on each path is not neccessary to be propotional to the physical distance since the number of routers on land is much more than the routers across oceans.


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
Running traceroute to `www.ucla.edu`, `www.u-tokyo.ac.jp`, `www.lancaster.ac.uk`.  

```
z5211336@drum00:~$ traceroute www.ucla.edu
traceroute to www.ucla.edu (164.67.228.152), 30 hops max, 60 byte packets
 1  cserouter1-trusted.cse.unsw.EDU.AU (129.94.208.251)  0.141 ms  0.105 ms  0.114 ms
 2  129.94.39.17 (129.94.39.17)  1.092 ms  1.086 ms  1.053 ms
 3  libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  1.578 ms ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.681 ms  1.493 ms
 4  ombcr1-po-6.gw.unsw.edu.au (149.171.255.169)  1.347 ms libcr1-po-6.gw.unsw.edu.au (149.171.255.201)  1.418 ms  1.409 ms
 5  unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.412 ms unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.515 ms  1.469 ms
 6  138.44.5.0 (138.44.5.0)  1.594 ms  1.452 ms  1.536 ms
 7  et-1-3-0.pe1.sxt.bkvl.nsw.aarnet.net.au (113.197.15.149)  2.381 ms  2.360 ms  2.371 ms
 8  et-0-0-0.pe1.a.hnl.aarnet.net.au (113.197.15.99)  95.444 ms  95.289 ms  95.286 ms
 9  et-2-1-0.bdr1.a.sea.aarnet.net.au (113.197.15.201)  146.681 ms  146.753 ms  146.715 ms
10  cenichpr-1-is-jmb-778.snvaca.pacificwave.net (207.231.245.129)  163.484 ms  163.421 ms  163.433 ms
11  hpr-lax-hpr3--svl-hpr3-100ge.cenic.net (137.164.25.73)  171.203 ms  171.205 ms  170.956 ms
12  * * *
13  bd11f1.anderson--cr00f2.csb1.ucla.net (169.232.4.4)  173.630 ms  171.594 ms bd11f1.anderson--cr001.anderson.ucla.net (169.232.4.6)  171.579 ms
14  cr00f2.csb1--dr00f2.csb1.ucla.net (169.232.4.53)  171.622 ms cr00f1.anderson--dr00f2.csb1.ucla.net (169.232.4.55)  171.657 ms  171.561 ms
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
z5211336@drum00:~$ traceroute www.u-tokyo.ac.jp
traceroute to www.u-tokyo.ac.jp (210.152.243.234), 30 hops max, 60 byte packets
 1  cserouter1-trusted.cse.unsw.EDU.AU (129.94.208.251)  0.139 ms  0.137 ms  0.112 ms
 2  129.94.39.17 (129.94.39.17)  1.070 ms  1.053 ms  1.032 ms
 3  libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  1.609 ms ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.526 ms  1.678 ms
 4  libcr1-po-5.gw.unsw.edu.au (149.171.255.165)  1.159 ms ombcr1-po-5.gw.unsw.edu.au (149.171.255.197)  1.318 ms  1.228 ms
 5  unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.381 ms  1.369 ms  1.335 ms
 6  138.44.5.0 (138.44.5.0)  1.432 ms  1.453 ms  1.465 ms
 7  et-0-3-0.pe1.bkvl.nsw.aarnet.net.au (113.197.15.147)  1.947 ms  1.980 ms  1.997 ms
 8  ge-4_0_0.bb1.a.pao.aarnet.net.au (202.158.194.177)  156.231 ms  156.382 ms  156.331 ms
 9  paloalto0.iij.net (198.32.176.24)  158.168 ms  158.184 ms  158.270 ms
10  osk004bb00.IIJ.Net (58.138.88.185)  289.198 ms  289.223 ms  289.222 ms
11  osk004ix51.IIJ.Net (58.138.106.126)  279.974 ms  279.918 ms  279.789 ms
12  210.130.135.130 (210.130.135.130)  280.030 ms  280.046 ms  280.045 ms
13  124.83.228.58 (124.83.228.58)  288.997 ms  289.022 ms  280.143 ms
14  124.83.252.178 (124.83.252.178)  285.947 ms  277.103 ms  285.917 ms
15  158.205.134.26 (158.205.134.26)  285.619 ms  285.827 ms  285.746 ms
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
z5211336@drum00:~$ traceroute www.lancaster.ac.uk
traceroute to www.lancaster.ac.uk (148.88.65.80), 30 hops max, 60 byte packets
 1  cserouter1-trusted.cse.unsw.EDU.AU (129.94.208.251)  0.217 ms  0.178 ms  0.150 ms
 2  129.94.39.17 (129.94.39.17)  1.106 ms  1.055 ms  1.090 ms
 3  ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.742 ms  1.710 ms libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  1.403 ms
 4  ombcr1-po-6.gw.unsw.edu.au (149.171.255.169)  1.259 ms libcr1-po-5.gw.unsw.edu.au (149.171.255.165)  1.296 ms  1.217 ms
 5  unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.303 ms unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.328 ms  1.357 ms
 6  138.44.5.0 (138.44.5.0)  1.442 ms  1.467 ms  1.414 ms
 7  et-1-3-0.pe1.sxt.bkvl.nsw.aarnet.net.au (113.197.15.149)  2.424 ms  2.235 ms  2.252 ms
 8  et-0-0-0.pe1.a.hnl.aarnet.net.au (113.197.15.99)  102.347 ms  102.260 ms  102.224 ms
 9  et-2-1-0.bdr1.a.sea.aarnet.net.au (113.197.15.201)  146.741 ms  147.279 ms  146.651 ms
10  abilene-1-lo-jmb-706.sttlwa.pacificwave.net (207.231.240.8)  147.195 ms  147.167 ms  146.768 ms
11  et-4-0-0.4079.rtsw.miss2.net.internet2.edu (162.252.70.0)  157.767 ms  157.784 ms  157.541 ms
12  et-4-0-0.4079.rtsw.minn.net.internet2.edu (162.252.70.58)  180.850 ms  180.845 ms  180.771 ms
13  et-1-1-5.4079.rtsw.eqch.net.internet2.edu (162.252.70.106)  188.502 ms  188.784 ms  188.770 ms
14  162.252.70.163 (162.252.70.163)  213.152 ms  188.920 ms  188.893 ms
15  ae-1.4079.rtsw.clev.net.internet2.edu (162.252.70.130)  198.006 ms  197.980 ms  197.515 ms
16  et-2-0-0.4079.rtsw.ashb.net.internet2.edu (162.252.70.54)  204.977 ms  205.403 ms  205.310 ms
17  ae-2.4079.rtsw.wash.net.internet2.edu (162.252.70.136)  205.461 ms  205.557 ms  205.680 ms
18  internet2-gw.mx1.lon.uk.geant.net (62.40.124.44)  280.438 ms  280.425 ms  280.670 ms
19  janet-gw.mx1.lon.uk.geant.net (62.40.124.198)  280.919 ms  280.795 ms  280.698 ms
20  ae29.londpg-sbr2.ja.net (146.97.33.2)  281.449 ms  281.037 ms  281.068 ms
21  ae31.erdiss-sbr2.ja.net (146.97.33.22)  284.913 ms  285.137 ms  284.906 ms
22  ae29.manckh-sbr2.ja.net (146.97.33.42)  286.665 ms  286.715 ms  286.641 ms
23  ae24.lanclu-rbr1.ja.net (146.97.38.58)  289.066 ms  289.204 ms  289.061 ms
24  lancaster-university.ja.net (194.81.46.2)  307.719 ms  307.120 ms  300.330 ms
25  isbfw01-isborder01.rtr.lancs.ac.uk (148.88.253.198)  289.303 ms  289.469 ms *
26  ismx-issrx.rtr.lancs.ac.uk (148.88.255.17)  293.785 ms  290.758 ms  291.006 ms
27  dc.iss.srv.rtrcloud.lancs.ac.uk (148.88.253.3)  312.759 ms  310.652 ms  310.524 ms
28  www.lancs.ac.uk (148.88.65.80)  290.909 ms !X  290.703 ms !X  290.946 ms !X
```


### 3.

`www.speeedtest.com.sg` has IP address `202.150.221.170`, 
`www.telstra.net` has IP address `203.50.5.178`. 

No, the reverse path doesn't go through the same route. It might because the routes go through the same ISP, but it's not neccessary to go through the same router. Hence, the IP addresses for forward and reverse routes are similar but not the same.

traceroute to speedtest:

```
traceroute to www.speedtest.com.sg (202.150.221.170), 30 hops max, 60 byte packets
 1  cserouter1-trusted.cse.unsw.EDU.AU (129.94.208.251)  0.233 ms  0.193 ms  0.169 ms
 2  129.94.39.17 (129.94.39.17)  1.218 ms  1.127 ms  1.173 ms
 3  ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.798 ms libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  1.570 ms ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.752 ms
 4  libcr1-po-5.gw.unsw.edu.au (149.171.255.165)  1.337 ms libcr1-po-6.gw.unsw.edu.au (149.171.255.201)  1.237 ms  1.340 ms
 5  unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.417 ms unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.401 ms  1.474 ms
 6  138.44.5.0 (138.44.5.0)  1.641 ms  1.581 ms  1.530 ms
 7  et-0-3-0.pe1.alxd.nsw.aarnet.net.au (113.197.15.153)  1.829 ms  1.928 ms  1.905 ms
 8  xe-0-0-3.pe1.wnpa.akl.aarnet.net.au (113.197.15.67)  24.588 ms  24.634 ms xe-0-2-1-204.pe1.wnpa.alxd.aarnet.net.au (113.197.15.183)  24.617 ms
 9  et-0-1-0.200.pe1.tkpa.akl.aarnet.net.au (113.197.15.69)  24.761 ms  24.805 ms  24.772 ms
10  xe-0-2-6.bdr1.a.lax.aarnet.net.au (202.158.194.173)  148.387 ms  148.386 ms  148.360 ms
11  singtel.as7473.any2ix.coresite.com (206.72.210.63)  170.484 ms  170.499 ms  170.466 ms
12  203.208.178.185 (203.208.178.185)  332.284 ms 203.208.172.173 (203.208.172.173)  148.423 ms  148.369 ms
13  203.208.153.121 (203.208.153.121)  310.093 ms 203.208.173.73 (203.208.173.73)  337.156 ms 203.208.177.110 (203.208.177.110)  237.028 ms
14  203.208.182.45 (203.208.182.45)  308.363 ms  308.109 ms  310.329 ms
15  203.208.177.110 (203.208.177.110)  224.735 ms 202-150-221-170.rev.ne.com.sg (202.150.221.170)  224.978 ms 203.208.177.110 (203.208.177.110)  240.213 ms
```

traceroute from speedtest:

```
traceroute to 129.94.209.30 (129.94.209.30), 30 hops max, 60 byte packets
 1  ge2-8.r01.sin01.ne.com.sg (202.150.221.169)  0.195 ms  0.212 ms  0.222 ms
 2  10.11.33.30 (10.11.33.30)  0.264 ms  0.274 ms  0.282 ms
 3  10.11.33.74 (10.11.33.74)  0.745 ms  0.757 ms  0.762 ms
 4  aarnet.sgix.sg (103.16.102.67)  225.569 ms  225.639 ms  225.653 ms
 5  xe-3-0-3.pe1.brwy.nsw.aarnet.net.au (113.197.15.206)  232.832 ms  232.847 ms  232.912 ms
 6  138.44.5.1 (138.44.5.1)  225.837 ms  225.935 ms  226.023 ms
 7  libcr1-te-1-5.gw.unsw.edu.au (149.171.255.102)  225.983 ms  226.061 ms  226.082 ms
 8  ombudnex1-po-1.gw.unsw.edu.au (149.171.255.202)  236.181 ms libudnex1-po-1.gw.unsw.edu.au (149.171.255.166)  224.035 ms ombudnex1-po-1.gw.unsw.edu.au (149.171.255.202)  236.084 ms
 9  ufw1-ae-1-3154.gw.unsw.edu.au (149.171.253.36)  236.452 ms  236.447 ms  236.421 ms
10  129.94.39.23 (129.94.39.23)  224.832 ms  224.691 ms  224.786 ms
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *
```

traceroute to telstra:

```
traceroute to www.telstra.net (203.50.5.178), 30 hops max, 60 byte packets
 1  cserouter1-trusted.cse.unsw.EDU.AU (129.94.208.251)  0.119 ms  0.101 ms  0.161 ms
 2  129.94.39.17 (129.94.39.17)  1.003 ms  1.110 ms  0.969 ms
 3  ombudnex1-vl-3154.gw.unsw.edu.au (149.171.253.35)  1.775 ms libudnex1-vl-3154.gw.unsw.edu.au (149.171.253.34)  1.973 ms  2.022 ms
 4  ombcr1-po-6.gw.unsw.edu.au (149.171.255.169)  1.364 ms  1.342 ms  1.355 ms
 5  unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.303 ms unswbr1-te-2-13.gw.unsw.edu.au (149.171.255.105)  1.301 ms unswbr1-te-1-9.gw.unsw.edu.au (149.171.255.101)  1.281 ms
 6  138.44.5.0 (138.44.5.0)  1.457 ms  1.421 ms  1.402 ms
 7  et-0-3-0.pe1.alxd.nsw.aarnet.net.au (113.197.15.153)  4.912 ms  3.634 ms  3.612 ms
 8  ae9.bb1.b.syd.aarnet.net.au (113.197.15.65)  2.028 ms  1.984 ms  1.988 ms
 9  gigabitethernet1-1.pe1.b.syd.aarnet.net.au (202.158.202.18)  1.973 ms  2.035 ms  1.954 ms
10  gigabitethernet3-11.ken37.sydney.telstra.net (139.130.0.77)  2.594 ms  2.696 ms  2.782 ms
11  bundle-ether2.chw-edge901.sydney.telstra.net (203.50.11.103)  2.898 ms bundle-ether13.ken-core10.sydney.telstra.net (203.50.11.94)  3.506 ms  3.977 ms
12  bundle-ether13.chw-core10.sydney.telstra.net (203.50.11.98)  3.446 ms bundle-ether10.win-core10.melbourne.telstra.net (203.50.11.123)  15.277 ms bundle-ether13.chw-core10.sydney.telstra.net (203.50.11.98)  2.812 ms
13  bundle-ether8.exi-core10.melbourne.telstra.net (203.50.11.125)  17.291 ms  17.245 ms 203.50.6.40 (203.50.6.40)  16.293 ms
14  bundle-ether2.exi-ncprouter101.melbourne.telstra.net (203.50.11.209)  14.485 ms  14.578 ms  13.830 ms
15  www.telstra.net (203.50.5.178)  14.239 ms  15.108 ms  15.101 ms
```

traceroute from telstra:

```
 1  gigabitethernet3-3.exi2.melbourne.telstra.net (203.50.77.53)  0.271 ms  0.216 ms  0.243 ms
 2  bundle-ether3-100.win-core10.melbourne.telstra.net (203.50.80.129)  2.866 ms  1.486 ms  2.118 ms
 3  bundle-ether12.ken-core10.sydney.telstra.net (203.50.11.122)  13.112 ms  11.980 ms  12.861 ms
 4  bundle-ether1.ken-edge901.sydney.telstra.net (203.50.11.95)  11.862 ms  11.856 ms  11.986 ms
 5  aarnet6.lnk.telstra.net (139.130.0.78)  11.612 ms  11.606 ms  11.612 ms
 6  ge-6-0-0.bb1.a.syd.aarnet.net.au (202.158.202.17)  11.863 ms  12.105 ms  11.736 ms
 7  ae9.pe2.brwy.nsw.aarnet.net.au (113.197.15.56)  12.861 ms  12.107 ms  11.986 ms
 8  et-3-1-0.pe1.brwy.nsw.aarnet.net.au (113.197.15.146)  12.113 ms  12.106 ms  12.111 ms
 9  138.44.5.1 (138.44.5.1)  12.362 ms  12.356 ms  12.237 ms
10  libcr1-te-1-5.gw.unsw.edu.au (149.171.255.102)  12.362 ms  12.356 ms  12.362 ms
11  libudnex1-po-1.gw.unsw.edu.au (149.171.255.166)  12.612 ms
12  ufw1-ae-1-3154.gw.unsw.edu.au (149.171.253.36)  13.106 ms  13.105 ms  13.005 ms
13  129.94.39.23 (129.94.39.23)  13.208 ms  13.226 ms  13.236 ms
```

## Exercise 4:



### 1. 
Physical distance from UNSW:

* to UQ: 743.01 km (456.09 mi)  
* to NUS: 6603.49 km (4103.22 mi)
* to TUB: 16104.74 km (1007.02 mi)

Shortest possible time T from UNSW:

* to UQ: 2.4767 ms
* to NUS: 22.011633 ms
* to TUB: 53.682467 ms



Possible reasons for greater than 2:

1. We assume that the packet moves at the speed of light, but in reality, the propagation speed is impossible to reach the speed of light. Hence, the delay will be greater.
2. Only propagation delay is counting for T, but actually there are also processing delay, queueing delay and transmission delay, so the mininum delay is greater than assumption.
3. The shortest distance measured using google map is straight-line distance, but in reality, the path that packets go through is not straight line, which means it takes longer for propagation, hence the delay is greater.


### 2.

The delay varies over time, because except for propagation delay, there are also: processing delay and transmission delay, which depends on the specific router; and queueing delay, which depends on the load of the router. Hence, the total delay varies over time.

### 3.
The one mainly depends on packet size is transmission delay as it is calculated from `packet size / bandwidth`. Queueing delay mainly depends on the load but it is revalent to packet size because is is calculated from `packets size * packets arrival rate / bandwidth`. 

Processing delay and propagation delay don't depend on packet size since processing delay depends on content complexity (as it has to scan and check error) and propagation delay depends on physical distance.

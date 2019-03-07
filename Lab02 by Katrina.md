# Lab02 by Katrina

## Exercise 2
### Q1.
`Status Code: 200`  
`Response Phrase: OK`

### Q2.

`Last-Modified: Mon, 04 Mar 2019 04:19:13 GMT\r\n`  
Response's DATE header: `Date: Thu, 07 Mar 2019 04:10:12 GMT\r\n`  
The last-modified date is the time the content modified by the server, and the Response's DATE header is the time that content arrived to the client. In this case, the lase-nidefued date us three days earlier than Response;s date.  

### Q3.
The connection is persistent. It refers to the line saying `Connection: keep-alive\r\n`  



### Q4.
`Content-Length: 727\r\n`  

### Q5.
```
0000   8c 85 90 8a 57 8e 7c 8b ca fb e5 a7 08 00 45 00   ....W.|.......E.
0010   04 98 41 1f 40 00 3c 06 bb ff ca 07 b1 2a c0 a8   ..A.@.<......*..
0020   01 67 00 50 cc 2f 19 b8 ea 55 d6 6a 30 df 80 18   .g.P./...U.j0...
0030   00 eb 36 aa 00 00 01 01 08 0a 04 92 ab 4c 12 37   ..6..........L.7
0040   b3 5e 48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f   .^HTTP/1.1 200 O
0050   4b 0d 0a 53 65 72 76 65 72 3a 20 41 70 61 63 68   K..Server: Apach
0060   65 0d 0a 4c 61 73 74 2d 4d 6f 64 69 66 69 65 64   e..Last-Modified
0070   3a 20 4d 6f 6e 2c 20 30 34 20 4d 61 72 20 32 30   : Mon, 04 Mar 20
0080   31 39 20 30 34 3a 31 39 3a 31 33 20 47 4d 54 0d   19 04:19:13 GMT.
0090   0a 45 54 61 67 3a 20 30 35 37 44 31 41 31 30 39   .ETag: 057D1A109
00a0   45 30 35 39 39 35 45 42 33 37 37 44 36 41 46 38   E05995EB377D6AF8
00b0   37 46 31 45 35 37 45 32 39 37 35 39 42 36 41 0d   7F1E57E29759B6A.
00c0   0a 58 2d 4f 43 53 50 2d 52 65 73 70 6f 6e 64 65   .X-OCSP-Responde
00d0   72 2d 49 44 3a 20 73 63 64 70 63 61 6f 63 73 70   r-ID: scdpcaocsp
00e0   31 30 0d 0a 43 6f 6e 74 65 6e 74 2d 4c 65 6e 67   10..Content-Leng
00f0   74 68 3a 20 37 32 37 0d 0a 43 6f 6e 74 65 6e 74   th: 727..Content
0100   2d 54 79 70 65 3a 20 61 70 70 6c 69 63 61 74 69   -Type: applicati
0110   6f 6e 2f 6f 63 73 70 2d 72 65 73 70 6f 6e 73 65   on/ocsp-response
0120   0d 0a 43 61 63 68 65 2d 43 6f 6e 74 72 6f 6c 3a   ..Cache-Control:
0130   20 70 75 62 6c 69 63 2c 20 6e 6f 2d 74 72 61 6e    public, no-tran
0140   73 66 6f 72 6d 2c 20 6d 75 73 74 2d 72 65 76 61   sform, must-reva
0150   6c 69 64 61 74 65 2c 20 6d 61 78 2d 61 67 65 3d   lidate, max-age=
0160   33 34 35 35 32 38 0d 0a 45 78 70 69 72 65 73 3a   345528..Expires:
0170   20 4d 6f 6e 2c 20 31 31 20 4d 61 72 20 32 30 31    Mon, 11 Mar 201
0180   39 20 30 34 3a 30 39 3a 30 30 20 47 4d 54 0d 0a   9 04:09:00 GMT..
0190   44 61 74 65 3a 20 54 68 75 2c 20 30 37 20 4d 61   Date: Thu, 07 Ma
01a0   72 20 32 30 31 39 20 30 34 3a 31 30 3a 31 32 20   r 2019 04:10:12 
01b0   47 4d 54 0d 0a 43 6f 6e 6e 65 63 74 69 6f 6e 3a   GMT..Connection:
01c0   20 6b 65 65 70 2d 61 6c 69 76 65 0d 0a 0d 0a 30    keep-alive....0
01d0   82 02 d3 0a 01 00 a0 82 02 cc 30 82 02 c8 06 09   ..........0.....
01e0   2b 06 01 05 05 07 30 01 01 04 82 02 b9 30 82 02   +.....0......0..
01f0   b5 30 81 9e a2 16 04 14 bb af 7e 02 3d fa a6 f1   .0........~.=...
0200   3c 84 8e ad ee 38 98 ec d9 32 32 d4 18 0f 32 30   <....8...22...20
0210   31 39 30 33 30 33 32 33 31 39 31 33 5a 30 73 30   190303231913Z0s0
0220   71 30 49 30 09 06 05 2b 0e 03 02 1a 05 00 04 14   q0I0...+........
0230   5e 02 1b 68 6c 5c d3 be 16 91 99 57 89 df c4 14   ^..hl\.....W....
0240   72 16 3d 03 04 14 bb af 7e 02 3d fa a6 f1 3c 84   r.=.....~.=...<.
0250   8e ad ee 38 98 ec d9 32 32 d4 02 10 06 a7 43 80   ...8...22.....C.
0260   d4 eb fe d4 35 b5 a3 f7 e1 6a bd d8 80 00 18 0f   ....5....j......
0270   32 30 31 39 30 33 30 33 32 33 31 39 31 33 5a a0   20190303231913Z.
0280   11 18 0f 32 30 31 39 30 33 31 30 32 33 31 39 31   ...2019031023191
0290   33 5a 30 0d 06 09 2a 86 48 86 f7 0d 01 01 0c 05   3Z0...*.H.......
02a0   00 03 82 02 01 00 3e 59 a1 e6 24 10 90 04 5a a2   ......>Y..$...Z.
02b0   54 ea 94 31 0a 40 0f df fe 8e 8d 6a df c2 f2 1f   T..1.@.....j....
02c0   5c d3 fc fd 5e 67 b1 c6 bd 6c 9d b7 55 2c eb 06   \...^g...l..U,..
02d0   d8 7c d9 75 c0 b0 06 c7 bd 4d 60 65 48 89 04 8e   .|.u.....M`eH...
02e0   42 13 51 8f 59 d2 cc 35 49 e6 32 0a a1 84 0e 88   B.Q.Y..5I.2.....
02f0   c1 e3 df ac 5d d9 60 78 f2 63 51 02 0f d2 e4 a8   ....].`x.cQ.....
0300   43 a2 44 65 59 5b e6 ec fc 47 c6 49 1c 85 94 f2   C.DeY[...G.I....
0310   4e b9 bd 7d 72 35 fe e4 e9 72 69 e3 20 0f 8c 0b   N..}r5...ri. ...
0320   43 ea 00 dc ac a7 73 7c 13 b7 5d d3 d7 f8 38 f4   C.....s|..]...8.
0330   3e de 21 21 a9 c6 5b 7c 92 5f 02 dc d5 0c d1 e9   >.!!..[|._......
0340   64 a7 eb f7 13 d7 c5 7b 15 81 87 88 7c 4a 13 92   d......{....|J..
0350   4b 75 3f 74 59 38 f6 46 b6 de ec 3c 5c e9 c1 95   Ku?tY8.F...<\...
0360   e6 a9 5b 7e c1 35 9c 15 80 33 5b 9c 7b 88 b0 74   ..[~.5...3[.{..t
0370   98 d3 50 88 3c 43 f0 4c e4 ea 89 90 e2 6a 87 53   ..P.<C.L.....j.S
0380   b0 7f 19 ff 9f cf b0 2f 1a 99 c6 94 c4 27 ac 30   ......./.....'.0
0390   cc cc 1c c5 af 0c 91 1f 34 5f 73 e3 48 4e 2a 84   ........4_s.HN*.
03a0   0d 74 cc 83 76 68 df 20 66 24 04 e6 a1 83 63 5f   .t..vh. f$....c_
03b0   18 c2 5a 31 38 f2 8c ee ac 02 fd 20 7c 43 23 64   ..Z18...... |C#d
03c0   61 0a d6 58 b4 18 fb bb 53 f7 49 25 f1 3f 75 80   a..X....S.I%.?u.
03d0   bf d4 47 13 03 6c e6 05 e5 ff 3d cd 18 c3 80 1d   ..G..l....=.....
03e0   b9 9c 20 6e 12 d1 ac bf 7a 55 dd 5f 36 e1 b4 67   .. n....zU._6..g
03f0   fa 70 b7 d7 a3 3a 4d e2 7b 07 02 4b eb d0 16 98   .p...:M.{..K....
0400   5f c8 79 f6 4d f9 0b 3e 3e 70 f7 b0 a0 e5 65 cb   _.y.M..>>p....e.
0410   ea f4 ff ef 97 60 86 c8 61 ba aa 13 4e 7d 67 f9   .....`..a...N}g.
0420   70 f1 4c 8c a0 90 7b 09 30 97 2c a6 b6 ff 8e 8f   p.L...{.0.,.....
0430   a2 40 07 0c e9 ac 51 09 82 f0 4e 0f c5 db 0b fc   .@....Q...N.....
0440   26 b9 7b a2 ce 98 16 89 a5 b2 d9 8e ea b7 0d d3   &.{.............
0450   2b 87 dd 69 f6 57 5a bb 37 01 d2 8a 43 29 03 21   +..i.WZ.7...C).!
0460   d3 f7 a8 9b 5f 6c d2 ac 97 42 7d f6 ee a9 de f6   ...._l...B}.....
0470   a5 a7 5f 37 ee 80 87 a7 69 f8 9c e4 33 d1 4a 24   .._7....i...3.J$
0480   8a e3 fd db 92 60 6c 4a 26 47 22 a3 ae 62 25 da   .....`lJ&G"..b%.
0490   6f e6 4e ca 61 85 b6 11 06 71 ff 62 77 57 18 ca   o.N.a....q.bwW..
04a0   26 43 56 a1 12 dd                                 &CV...
```


## Exercise 4
### Q1.
`If-Modified-Since` is contained in the second HTTP GET request but not the first HTTP GET request.  


### Q2.
Yes.  
`Last-Modified: Tue, 23 Sep 2003 05:35:00 GMT\r\n`  


### Q3.
Yes.  
`If-Modified-Since: Tue, 23 Sep 2003 05:35:00 GMT\r\n`  
`If-None-Match: "1bfef-173-8f4ae900"\r\n`  
It indicates the "version" of the content

### Q4.
`Status Code: 304`  
`Response Phrase: Not Modified`  

No, it didn't return the contents. As `Status Code: 304` indicates that the resource has not been modified since the previous transmission, so there is no need to retransmit the requested resource to the client.

### Q5.
`ETag: "1bfef-173-8f4ae900"\r\n`  
It's used by the server to check if the same content needs a new copy of the resource. In this case, the `If-None-Match` header in the 2nd request matches the `ETag` in the 1st respense, which means the browser was requesting the same version as previous request, so the response sent an empty body back and the browser used cached copy of the content.  
Similaly, the `ETag` in the 2nd response is used for comparing in next requesting content from browser, as the current version of content is the same as the 1st response, the `ETag` wasn't change.


## Exercise 5

see `PingClient.py`


# Lab5 by Katrina
## Exercise 1
### Q1.
The maximum congestion window is 100 packets. When TCP reaches the maximum and finds that there is packet loss, it reduces the window size to 1, halves the threshold and implements Slow Start, which increasing the window size in exponential rate. Once the window size reaches the threshold, it switches from Slow Start to AIMD.

### Q2. 
`Throuput = data / time`  
**Pkt/sec**: From the graph, the average throughput is approx. 190 packets/sec.  
**bps (bits/sec)**: As packet size = IP payload + IP header = (TCP payload + TCP header) + IP header, the average throughput can be converted by `190 * (500+20+20) * 8 = 28800 bits/sec`.

## Q3.
From the graph with maximum window size of 150, observe that every time when TCP drop packets, the window size is approx. 68. Hence, try setting the max. window size to 68 and find that the TCP is sill oscillating, which means TCP drops packets when the window size has not reached the max. As a result, try decreasing the max. window size. Consequently, when the max window size is **66**, TCP stops oscillating.  

At this point, the average throughput is approx. **210 packets/second**, which is `210 * (500+20+20) * 8 =  907200 bits/sec`. It only occupy about 90.7% of the link capacity.  
 

## Q4. 
TCP Window size:  
**Tahoe**: Will set window size to 1 when there is timeout.  
**Reno**: Only halve the window size when there is timeout.  

Average throughput:  
**Tahoe**: Approx. 190 packets/sec  
**Reno**: Approx 200 packets/sec  

## Exersise 3
### Q1.
Blue represents TCP and red represents UDP as the red send packets in consistent rate but the blue send packets with flexible window size.

### Q2.
UDP is much faster than TCP. This is because TCP has congestion control and it sometimes reduces the window size, while UDP sends data in consistent rate.

### Q3.
**Advantages**: efficient, very quick as it doesn't control the rate that sending packets.   
**Disadvantages**: Packet loss might happen during the transmittion, hence the application that using UDP has to implement reliable data trasmission mechanism such as timer.   

If everybody started using UDP, as there is no congestion control, it will rapidly increase the prossibility of congestion collapse, causing more packets loss.



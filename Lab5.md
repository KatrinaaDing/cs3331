# Lab5 by Katrina
## Exercise 1
### Q1.
The maximum congestion window is 100. It reduce the window size to 1, because it has to re find the maximum congestion window (maximum capacity of the link). Then it halves the threshold and implements Slow Start, which increasing the window size in exponential rate. Once the window size reach the threshold, it switches from Slow Start to **AIMD**.

### Q2. 
`Throuput = data / time`  
Known that `time = 60 second`.   
And `Data =  150 * `  
From the graph, the average throughput is approx. 180 bytes/sec

## Q3.
???

## Q4. 
TCP Window size:  
**Tahoe**: Will set window size to 1 when there is timeout.  
**Reno**: Only halve the window size when there is timeout.  

Average throughput:  
**Tahoe**: Approx. 180 packets/sec  
**Reno**: Approx 200 packets/sec  

## Exersise 2
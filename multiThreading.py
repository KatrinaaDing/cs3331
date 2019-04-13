import threading


t1 = threading.Thread(target=function1, args=(argument tupple))
t2 = threading.Thread(target=function2, args=(argument tupple))


t1.start()
t2.start() 

t1.join() # join the pool and excute simutanously
t2.join() # will wait untill two threads done

threading.Lock(): within a lock, only one thread can run at a time
semaphore: allow more than one lock 
import csv
import time

MSS = 246
seq = 0
lastRead = -1

fp = open('0258.pdf', 'rb')
wp = open('testcopy.pdf', 'ab')
log_fp = open('testLog.txt', 'a')

start = time.time()
while True:
	print(f"\n----------seq {seq}---------")
	
	print(f"reading file")
	content = fp.read(MSS)
	print(content)
	if content == b"":
		break
	log_fp.write(f'read\t{seq}\t{MSS}\t{len(content)}\t{time.time()-start}\n')
	print("writing file")
	wp.write(content)
	print('------------------------------\n')
	seq += 1

fp.close()
wp.close()

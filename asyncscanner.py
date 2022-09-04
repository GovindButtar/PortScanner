#!/bin/python3
import asyncio
import socket
name = input("Give the website name to be scanned: ")
open_ports = []
ports = []
try:
	
	ip = socket.gethostbyname(name)
except:
	ip = input("Entering in the website name did not work, instead enter in the ip address for the website, which can be done by putting nmap hostname: ")
	
#input min port
min = input("What is the minimum port that you want scanned?: ")
#input max port 
max = input("What is the maximum port that you want scanned?: ")

def runScanner(tasks, *, loop=None):
	if loop is None:
		loop = asyncio.get_event_loop()
	    # waiting for all tasks
	return loop.run_until_complete(asyncio.wait(tasks))
    
async def scanner(ip, port, loop=None):
	loop = asyncio.get_event_loop()
	fut = asyncio.open_connection(ip, port)
	try:
		reader, writer = await asyncio.wait_for(fut, timeout = 1) 
		print("{}:{} Connected".format(ip, port))
	except asyncio.TimeoutError:
		pass
	except Exception as exc:
		print('Error {}:{} {}'.format(ip, port, exc))

def scan(ip, ports):
	loop = asyncio.get_event_loop()
	runScanner([scanner(ip, port) for port in ports])
for i in range(int(min), int(max)+1):
	ports.append(i)
scan(ip, ports)

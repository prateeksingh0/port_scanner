import socket


def scan(target, ports):
	print("\nStarting Scan For", str(target))
	x = 0
	for port in range(1, ports):
		if scan_port(target, port):
			x+=1
	if x==0:
	   print("All",ports,"ports are closed for", target,"\n")


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened", str(port))
		return 1
	except:
		pass



targets = input("[*] Enter Tragets To Scan(splits them by ','): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
while ports<0 or ports>65535:
	print("Enter valid ports number.")
	ports = int(input("[+] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)

else:
	scan(targets, ports)

print("\nScan Completed.")

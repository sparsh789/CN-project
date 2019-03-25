import socket
import os
import sys
import datetime
import hashlib

def shortlist(c,date1,time1,date2,time2):
	date11 = tuple(map(int,date1.split('-')))
	time11 = tuple(map(int,time1.split(':')))
	date22 = tuple(map(int,date2.split('-')))
	time22 = tuple(map(int,time2.split(':')))
	strtime = datetime.datetime(date11[0],date11[1],date11[2],time11[0],time11[1],time11[2])
	endtime = datetime.datetime(date22[0],date22[1],date22[2],time22[0],time22[1],time22[2])
	files = filter(os.path.isfile, os.listdir( os.curdir ) )
	if len(files)==0:
		ans = "No files in current directory"
		c.send(ans.encode())
		print ans
	else:
		for f in files:
			ftime = datetime.datetime.fromtimestamp(os.path.getmtime(f))
			name, ext = os.path.splitext(f)
			if ftime>strtime and ftime<endtime:
				ans = "name: " + f + "   size: " + str(os.path.getsize(f)) + "   timestamp: " + ftime.strftime('%Y-%m-%d %H:%M:%S') + "   extension: " + ext
				c.send(ans.encode())
				print ans
	rem = '||end||';
	c.send(rem.encode())
	if len(files)!=0:
		print 'Sent detail successfully'

#### BONUS #####
def shortlist_specific(c,date1,time1,date2,time2,type1):
	date11 = tuple(map(int,date1.split('-')))
	time11 = tuple(map(int,time1.split(':')))
	date22 = tuple(map(int,date2.split('-')))
	time22 = tuple(map(int,time2.split(':')))
	strtime = datetime.datetime(date11[0],date11[1],date11[2],time11[0],time11[1],time11[2])
	endtime = datetime.datetime(date22[0],date22[1],date22[2],time22[0],time22[1],time22[2])
	files = filter(os.path.isfile, os.listdir( os.curdir ) )
	n = 0
	type1 = type1[1:5]
	for f in files:
		ftime = datetime.datetime.fromtimestamp(os.path.getmtime(f))
		name, ext = os.path.splitext(f)
		if ftime>strtime and ftime<endtime and ext==type1:
			ans = "name: " + f + "   size: " + str(os.path.getsize(f)) + "   timestamp: " + ftime.strftime('%Y-%m-%d %H:%M:%S') + "   extension: " + ext
			c.send(ans.encode())
			print ans
			n = n+1
	if n!=0:
		print 'Sent detail successfully'
	else:
		ans = "No files of given format in current directory"
		c.send(ans.encode())
		print ans
	rem = "||end||"
	c.send(rem.encode())

###############

def longlist(c):
	files = filter(os.path.isfile, os.listdir( os.curdir ) )
	if len(files)==0:
		ans = "No files in current directory"
		c.send(ans.encode())
		print ans
	else:
		for f in files:
			ftime = datetime.datetime.fromtimestamp(os.path.getmtime(f))
			name, ext = os.path.splitext(f)
			ans = "name: " + f + "   size: " + str(os.path.getsize(f)) + "   timestamp: " + ftime.strftime('%Y-%m-%d %H:%M:%S') + "   extension: " + ext
			c.send(ans.encode())
			print ans
	rem = '||end||';
	c.send(rem.encode())
	if len(files)!=0:
		print 'Sent detail successfully'

###### BONUS ####
def longlist_specific(c):
	files = filter(os.path.isfile, os.listdir( os.curdir ) )
	n = 0;
	for f in files:
		ftime = datetime.datetime.fromtimestamp(os.path.getmtime(f))
		name, ext = os.path.splitext(f)
		flag = 0
		if ext == '.txt':
			term = "programmer"
			file = open(f)
			for line in file:
				line = line.strip().split(' ')
				if term in line:
					#print line
					flag = 1
					break;
			file.close()
		if flag==1:
			ans = "name: " + f + "   size: " + str(os.path.getsize(f)) + "   timestamp: " + ftime.strftime('%Y-%m-%d %H:%M:%S') + "   extension: " + ext
			c.send(ans.encode())
			print ans
			n = n+1
	if n!=0:
		print 'Sent detail successfully'
	else:
		ans = "No text files containing word programmer"
		c.send(ans.encode())
		print ans
	rem = '||end||';
	c.send(rem.encode())
###########

def Filehashsingle(c,file):
	hash_md5 = hashlib.md5()
	try:
		with open(file, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		ans = "hash: " + hash_md5.hexdigest()+ "   timestamp: " + datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
		c.send(ans.encode())
		print 'Sent detail successfully'
	except:
		ans = "File does not exist"
		print ans
		c.send(ans.encode())

def Filehashmultiple(c):
	files = filter(os.path.isfile, os.listdir( os.curdir ) )
	for file in files:
		hash_md5 = hashlib.md5()
		with open(file, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		ans = "name: "+file +"   hash: " + hash_md5.hexdigest() + "   timestamp: " + datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S')
		c.send(ans.encode())
	rem = '||end||'
	c.send(rem.encode())
	print 'Sent detail successfully'

def sendFile(c,file):
	try:
		f = open(file,'rb')
	except:
		print('error opening file or file does not exist')
	l = f.read(1024)
	while (l):
		#print l
		c.send(l)
		l = f.read(1024)
	print 'file sent'
	f.close()
	hash_md5 = hashlib.md5()
	with open(file, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	ans = "name: " + file + "   size: " + str(os.path.getsize(file)) + "   timestamp: " + datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S') + "   hash: " + hash_md5.hexdigest()
	c.send(ans.encode())

def sendFile_udp(c,file,port_udp,host):
	udp_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = (host, port_udp)
	try:
		f=open(file,'rb')
	except:
		print('error opening file or file does not exist')
	l=f.read(1024)
	while(l):
		if(udp_soc.sendto(l,dest)):
			l = f.read(1024)
	udp_soc.close()
	f.close()
	hash_md5 = hashlib.md5()
	with open(file, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	ans = "name: " + file + "   size: " + str(os.path.getsize(file)) + "   timestamp: " + datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S') + "   hash: " + hash_md5.hexdigest()
	c.send(ans.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "Socket successfully created"
port=12345
port_udp = 12347
host = socket.gethostname()
s.bind((host, port))
s.listen(5)
while True:
	try:
		c,addr=s.accept()
		s.settimeout(.5)
		print("Connection from: " + str(addr))

		while True:
			val=c.recv(1024).decode()
			#print val
			#val=val.decode()
			vald = val.strip().split(' ')
			if len(vald)>=6 and vald[1]=='shortlist':
				if len(vald)==6:
					shortlist(c,vald[2],vald[3],vald[4],vald[5])
				elif len(vald)==7:
					shortlist_specific(c,vald[2],vald[3],vald[4],vald[5],vald[6])
			elif len(vald)>=2 and vald[1]=='longlist':
				if len(vald)==2:
					longlist(c)
				elif len(vald)==3:
					longlist_specific(c)
			elif len(vald)>=2 and vald[0]=='FileHash':
				if len(vald)==3 and vald[1]=='verify':
					Filehashsingle(c,vald[2])
				elif len(vald)==2 and vald[1]=='checkall':
					Filehashmultiple(c)
			elif len(vald)==4 and vald[0] == 'FileDownload':
				if vald[3]=='TCP':
					sendFile(c,vald[1])
				elif vald[3]=='UDP':
					sendFile_udp(c,vald[1],port_udp,host)
			else:
				print 'Invalid Command'
				break
	except KeyboardInterrupt:
		print 'Socket Closed'
		s.close()
		sys.exit()
	except socket.timeout:
		print 'Client Disconnected'
		s.settimeout(None)
	c.close()
s.close()
# Introduction

In this project we have implemented a file sharing protocol similar to Dropbox with
support for download from server and indexed searching.
	
	* The system has one server and one client. Server is listening for client and
	after connection between them (Used TCP as default protocol) client can
	request for information about files and download them.
	* File transfer should incorporate MD5 checksum to handle file transfer errors


# Commands and Results

First Run ‘ python server.py ‘ in one terminal to start server. Then run ‘ python
client.py ‘ in separate terminal to make and connect client to server.
Then run following commands in client side to get data from server:
	
	* IndexGet shortlist <starttimestamp> <endtimestamp>
	Output: Return ‘name’ , ‘size’ , ‘timestamp’ and ‘type’ of the files between
	the start and end time stamps to client.
	* BONUS​ - ​ IndexGet shortlist <starttimestamp> <endtimestamp> *.txt or *.pdf
	Output: Return only *.txt , *.pdf files between specified time stamps to client.
	* IndexGet longlist
	Output: Return ‘name’, ‘size’ , ‘timestamp’ and ‘type’ of all files (not
	directories) present in current working directory of server to client.
	* BONUS​ - ​ IndexGet longlist specific
	output: Return longlist for only *.txt file containing word “Programmer” in it.● FileHash verify <FileName>
	Output:​ Return checksum and last modified timestamp of the input file to
	client.
	* FileHash checkall
	Output: Return filename , checksum and last modified timestamp of all the
	files in the current working directory of server.
	* FileDownload Path1 Path2 TCP/UDP
	Path1 - path of file to be downloaded
	Path2 - path of file where above file should be downloaded
	Output: Download file specified in Path1 and also returns filename , filesize
	,last modified timestamp and the MD5hash of the requested file.
	* Exit ​ - to stop client and server.
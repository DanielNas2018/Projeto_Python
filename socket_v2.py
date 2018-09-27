import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print(s)
	server = 'pythonprogramming.net'
	port = 80
	server_ip = socket.gethostbyname(server)
	print()
	print(server_ip)
	request = "GET/ HTTP/1.1\nHOST: "+server+"\n\n"
	s.connect((server,port))
	s.send(request.encode())
	result = s.recv(4064)
	print()
	print(result)

if __name__ == '__main__':
	main()
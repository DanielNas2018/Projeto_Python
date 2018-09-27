import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print(s)
	server = input("Informe o dominio que deseja verificar o ip: ")
	port = 80
	server_ip = socket.gethostbyname(server)
	print()
	print(server_ip)	

if __name__ == '__main__':
	main()
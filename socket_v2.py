import socket

def main():
	server = input("Informe o dominio que deseja verificar o ip: ")
	port = 80
	server_ip = socket.gethostbyname(server)
	print()
	print(server_ip)

if __name__ == '__main__':
	main()




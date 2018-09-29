import socket



class Rede():
	def main():
		server = input("Informe o dominio que deseja verificar o ip: ")
		server_ip = socket.gethostbyname(server)
		print()
		print(server_ip)

	if __name__ == '__main__':
		main()

	def IP():
		server_ip = socket.gethostname()
		print()
		print("Nome da Maquina: ",server_ip)

	if __name__ == '__main__':
		IP()





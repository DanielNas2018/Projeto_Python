import socket

class Rede:
	def IP(self, dominio):	
		self.dominio = dominio	
				
	def obterRede(self):
		return self.dominio	

	def HOST(self,host):
		self.host = host
		 
	def obterHost(self):
		return  self.host

	
dominio = input("Informe o dominio que deseja verificar o ip: ")
server_ip = socket.gethostbyname(dominio)
host = socket.gethostname()

rede = Rede()
rede.IP(server_ip)
print(rede.obterRede())
rede.HOST(host)
print("\nNome da sua Maquina: " + rede.obterHost())
print()







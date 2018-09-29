import socket #importando socket

class Rede:	#criando classe rede para organização das funções

	def IP(self, dominio):	#função IP, pega o valor enviando pelo o usuario e inseri dentro da variavel dominio
		self.dominio = dominio	
				
	def obterRede(self):	#função obterRede, recebe o ip do dominio retorna para o usuario
		return self.dominio	

	def HOST(self,host):	#função HOST, pega o nome da maquina
		self.host = host
		 
	def obterHost(self):	#função obterHost, envia o nome para o usuario
		return  self.host	
	
def Dominio():	#Metodo criado para receber os dados do usuario e enviar para a classe Rede
	dominio = input("Informe o dominio que deseja verificar o ip: ") #recebe o dominio que o usúario digitar
	server_ip = socket.gethostbyname(dominio)#atráves do comando "gethostbyname" o dominio que o usuario 
	#digitou, será pego apenas o ip e jogago para dentro da variavel server_ip
	rede = Rede() #instanciando a classe a Rede
	rede.IP(server_ip) 	#envia o ip
	print(rede.obterRede())	#Retorna o ip
if __name__ =='__main__':	#Parar a aplicação
	Dominio() #chama a aplicaçao

def nomeMaquina():
	host = socket.gethostname()
	rede = Rede()
	rede.HOST(host)
	print("\nNome da sua Maquina: " + rede.obterHost())
	print()	
if __name__ =='__main__':
	nomeMaquina()







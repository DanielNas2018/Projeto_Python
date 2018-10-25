import socket
import threading
import sys
import pickle




class Servidor():

	def servidor_Chamando(self, port, host = 'localhost' ):

		self.clientes = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		aceitar = threading.Thread(target=self.aceitarCon)
		processar = threading.Thread(target=self.processarCon)

		aceitar.daemon = True
		aceitar.start()

		processar.daemon = True
		processar.start()	 

		print("\nServidor Ativo\n")
		while True:
			msg = input('->')
			if msg == 'Exit':
				self.sock.close()
				sys.exit()
			elif msg == 'Menu':
				projeto.Organiza()			
			else:
				pass

	def msg_to_all(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceitarCon(self):
		print("\nConexão Iniciada")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				 pass
				 
	def processarCon(self):
		print("\nProcessar Iniciado\n")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.msg_to_all(data,c)
					except:
						pass

def Servico():
	try:
		s = Servidor()
		s.servidor_Chamando(port = input("\nInforme o numero da Porta: \n"))
	except:
		pass
if __name__ =='__main__':
	Servico()






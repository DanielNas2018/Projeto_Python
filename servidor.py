import socket
import threading
import sys
import pickle


class Servidor():

	def __init__(self, host = "localhost", port=3000):

		self.clientes = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		aceitar = threading.Thread(target = self.aceitarCon)
		processar = threading.Thread(target = self.processarCon)

		aceitar.daemon = True
		aceitar.start()

		processar.daemon = True
		processar.start()

		while True:
			msg = input('->')
			if msg == 'sair':
				self.sock.close()
				sys.exit()
			else:
				pass


	def msg_toa_all(self, msg, cliente):
		for c in self.clientes:
			try:
				if c !=cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceitarCon(self):
		print("aceitarCon Iniciado")
		while True:
			try:
				conn, addr = self.sock.aceitar()
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				 pass
				 
	def processarCon(self):
		print("Processar Iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(1024)
						if data:
							self.msg_to_all(data,c)
					except:
						pass


s = Servidor()



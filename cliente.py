import threading
import socket
import sys
import pickle
import projeto

class Cliente():

	def cliente_Chamando(self ,host, port = 4000):

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		msg_recv = threading.Thread(target = self.msg_recv)

		msg_recv.daemon = True
		msg_recv.start()

		while True:
			nomeMaquina = socket.gethostname()
			msg = input(nomeMaquina + ' ->')
			if msg != 'Exit':
				self.send_msg(msg)				
			else:
				self.sock.close()				
				sys.exit()



	def msg_recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_msg(self, msg):
		self.sock.send(pickle.dumps(msg))


def Chat():
	try:	
		c = Cliente()
		c.cliente_Chamando(host = input("\nInforme o numero do IP do Cliente: \n"))
	except:
		pass


if __name__ =='__main__':
	Chat()

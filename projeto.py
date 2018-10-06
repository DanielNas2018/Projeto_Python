import os
import socket_v2
import cliente

clear = lambda: os.system("cls")

def Organiza():
	while True:
		print("\n\n-------------------Menu--------------------------")
		print('''
			[ 1 ] - Verificar o IP do dominio
			[ 2 ] - Verificar o nome da sua Maquina
			[ 3 ] - Utilizar o Chat
			[ 4 ] - Sair do programa''')

		opcao =  int(input("\nEscolha a sua opção: "))

		clear()

		if opcao == 1:		
			socket_v2.Dominio()

		elif opcao == 2:
			socket_v2.nomeMaquina()

		elif opcao == 3:
			while True:
				print('''Confirme se o servidor está ativo antes de acessar o chat
				[ 1 ] - Continuar
				[ 2 ] - Voltar''')

				opcao =  int(input("\nEscolha a sua opção: "))

				if opcao == 1:
					print("Acessando o chat, para sair do chat digite 'exit'")
					print()
					cliente.Cliente()

				elif(opcao > 2):
					print("\nOpção invalida, tente novamente!\n")
				else:
					print("\nVoltando para o Menu\n")
					break
					o = Organiza()

		elif (opcao > 4):
			print("\nOpção invalida, tente novamente!\n")
		else:
			print("\nSaindo do programa\n")
			break

if __name__ == '__main__':
	Organiza()
import os
import socket_v2
import cliente
import servidor

clear = lambda: os.system("cls")

def Organiza():

	while True:

		print("\n\n-------------------Menu--------------------------")
		print('''
			[ 1 ] - Verificar o IP do dominio
			[ 2 ] - Verificar o nome da sua Maquina
			[ 3 ] - Habilitando o Servidor
			[ 4 ] - Utilizar o Chat
			[ 5 ] - Sair do programa''')

		opcao =  int(input("\nEscolha a sua opção: "))

		clear()

		if opcao == 1:		
			socket_v2.Dominio()

		elif opcao == 2:
			socket_v2.nomeMaquina()

		elif opcao == 3:

			while True:

				print('''Selecione a opção desejada
				[ 1 ] - Continuar
				[ 2 ] - Voltar''')

				opcao =  int(input("\nEscolha a sua opção: \n"))

				if opcao == 1:
					print('''\nAcessando o Servidor!!!\nPara fechar o servidor digite "Exit"\nVoltar ao menu principal digite "Menu" ''')
					print()									
					servidor.Servico()
					break
				elif(opcao > 2):
					print("\nOpção invalida, tente novamente!\n")
				else:
					print("\nVoltando para o Menu\n")
					break
					

		elif opcao == 4:
			while True:
				print('''Selecione a opção desejada
				[ 1 ] - Continuar
				[ 2 ] - Voltar''')

				opcao =  int(input("\nEscolha a sua opção: \n"))

				if opcao == 1:
					print("\nAcessando o chat, para fechar o chat digite 'Exit'\n")
					print()					
					cliente.Chat()
					break

				elif(opcao > 2):
					print("\nOpção invalida, tente novamente!\n")
				else:
					print("\nVoltando para o Menu\n")
					break
					

		elif (opcao > 5):
			print("\nOpção invalida, tente novamente!\n")
		else:
			print("\nSaindo do programa\n")
			break

if __name__ == '__main__':
	Organiza()
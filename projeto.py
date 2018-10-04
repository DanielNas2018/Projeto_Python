import os
import socket_v2

clear = lambda: os.system("cls")

while True:
	print("\n\n-------------------Menu--------------------------")
	print('''
		[ 1 ] - Verificar o IP do dominio
		[ 2 ] - Verificar o nome da sua Maquina
		[ 3 ] - Sair do programa''')

	opcao =  int(input("\nEscolha a sua opção: "))

	clear()

	if opcao == 1:		
		socket_v2.Dominio()
	elif opcao == 2:
		socket_v2.nomeMaquina()
	elif (opcao > 3):
		print("Opção invalida, tente novamente!")
	else:
		print("Saindo do programa")
		break
import os

clear = lambda: os.system("cls")

while True:
	print("\n\n-------------------Menu--------------------------")
	print('''
		[ 1 ] - Verificar se o IP está ativo
		[ 2 ] - Segundo numero
		[ 3 ] - Terceiro numero
		[ 4 ] - Sair do programa''')

	opcao =  int(input("\nEscolha a sua opção: "))

	clear()

	if opcao == 1:		
		ip = input("infore o ip que deseja verificar: ")
		print(ip)
	elif opcao == 2:
		print("\n\nSegundo numero")
	elif opcao == 3:
		print("\n\nTerceiro numero")
	elif (opcao > 4):
		print("Opção invalida, tente novamente!")
	else:
		print("Saindo do programa")
		break
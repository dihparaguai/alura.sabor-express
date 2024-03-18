import os

print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')
print('\n')

# //comentario
opcao_escolhida = int(input('digite a opcao digitada: '))
print(f'voce escolheu a opcao: {opcao_escolhida}\n')

# declarando uma funcao
def encerrar_aplicacao():
    os.system('cls') # limpa o terminal do windows
    os.system('clear') #limpa o terminal do mac
    print('encerrando o programa')

# 'else if' == 'elif'
if opcao_escolhida == 1:
    print('cadastrar restaurante')
elif opcao_escolhida == 2:
    print('listar resutaurantes')
elif opcao_escolhida == 3:
    print('ativar resutaurante')
else:
    encerrar_aplicacao()
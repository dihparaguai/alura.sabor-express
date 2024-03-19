import os

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

# declarando uma funcao
def encerrar_aplicacao():
    os.system('cls') # limpa o terminal do windows
    # os.system('clear') # limpa o terminal do mac
    print('encerrando o programa')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')
    print('\n')

# ao digita uma opcao fora do programa
def opcao_invalida():
    os.system('cls')
    print('opcao invalida: escolha uma opcao entre 01 e 04')
    # um input sozinho apenas para aguardar o aperto de alguma tecla
    input('digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcao():
    # semelhante ao try-catch
    try:
        # //comentario
        opcao_escolhida = int(input('digite a opcao digitada: '))
        print(f'voce escolheu a opcao: {opcao_escolhida}\n')
        
        # 'else if' == 'elif'
        if opcao_escolhida == 1:
            print('cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('listar resutaurantes')
        elif opcao_escolhida == 3:
            print('ativar resutaurante')
        elif opcao_escolhida == 4:
            encerrar_aplicacao()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# metodo principal
def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
import os

# uma lista ligada respresentado por chave, separados por virgula
# um dicionario, com chave valor, separados por dois pontos
# cada elemento da lista eh um dicionario com 3 informacoes cada
restaurantes = [{'nome':'restaurante01', 'cagegoria' : 'categoria01', 'situacao' : 'ativo'},
                {'nome':'restaurante02', 'cagegoria' : 'categoria02', 'situacao' : 'ativo'},
                {'nome':'restaurante03', 'cagegoria' : 'categoria03', 'situacao' : 'inativo'},              
]

def exibir_nome_programa():
    # usar 3 aspas, podemos escrever da mesma forma que sera exibido no console
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')

# declarando uma funcao
def encerrar_aplicacao():
    os.system('cls') # limpa o terminal do windows
    # os.system('clear') # limpa o terminal do mac
    print('encerrando o programa')

def titulo_menu(titulo):
    os.system('cls')
    print(f'{titulo}\n')

def voltar_menu():
    input('\ndigite uma tecla para voltar ao menu principal\n')
    main()

# ao digita uma opcao fora do programa
def opcao_invalida():
    titulo_menu('opcao invalida: escolha uma opcao entre 01 e 04')
    # um input sozinho apenas para aguardar o aperto de alguma tecla
    voltar_menu()

def cadastrar_novo_restaurante():
    titulo_menu('cadastro de novos resutaures')
    nome_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'digite a categoria do restaurante {nome_restaurante}: ')

    # append serve para adiciona um item a lista
    restaurantes.append(nome_restaurante)
    # interpolacao de string
    print (f'\no restaurante \'{nome_restaurante}\' foi cadastrado com sucesso')
    # ao terminar o cadastro, voltar para a tela inicial
    voltar_menu()

def listar_todos_restaurantes():
    titulo_menu('listagem de todos os restaurantes cadastrados')
    # para cada restaurante na lista de restaurantes, print
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = restaurante['situacao']
        print(f'- {nome_restaurante} | {categoria} | {situacao}')
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')
    print('\n')

def escolher_opcao():
    # semelhante ao try-catch
    try:
        # //comentario
        opcao_escolhida = int(input('digite a opcao digitada: '))
        # print(f'') para fazer interpolacao de string
        print(f'voce escolheu a opcao: {opcao_escolhida}\n')

        # 'else if' == 'elif'
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_todos_restaurantes()
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

# define este arquivo como arquivo principal para iniciar o programa
if __name__ == '__main__':
    main()
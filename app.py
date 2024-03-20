'''
DOCSGTRING = Para documentar e informar previamente funcionalidades 
Nome do Programa: Sabor Express
Desenvolvido por: Diego Paraguai de Carvalho juntamente com Alura
Data de Criacao: 2024-03-18
Objetivo: Desenvolver a parte do back-end, para cadastrar, listar e atuaizar restaurantes
'''
import os

# uma lista ligada respresentado por chave, separados por virgula
# um dicionario, com chave valor, separados por dois pontos
# cada elemento da lista eh um dicionario com 3 informacoes cada
restaurantes = [{'nome':'restaurante01', 'categoria':'categoria01', 'ativo':False},
                {'nome':'restaurante02', 'categoria':'categoria02', 'ativo':True},
                {'nome':'restaurante03', 'categoria':'categoria03', 'ativo':False},              
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
    linha = '*' * (len(titulo) + 4)
    print(linha)
    print(f'{titulo}')
    print(linha)

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
    # esta sendo adicionado um dicionario na lista
    restaurantes.append({'nome' : nome_restaurante , 'categoria' : categoria_restaurante, 'situacao' : False})
    # interpolacao de string
    print(f'\no restaurante \'{nome_restaurante}\' foi cadastrado com sucesso')
    # ao terminar o cadastro, voltar para a tela inicial
    voltar_menu()

def listar_todos_restaurantes():
    titulo_menu('listagem de todos os restaurantes cadastrados')
    print(f'{'nome do restaurante'.ljust(23)} | {'categoria'.ljust(20)} | status')
    # para cada restaurante na lista de restaurantes, print
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        # operador ternario diferenciado: se verdadeiro, condicao, se falso
        ativo = 'ativado' if restaurante['ativo'] else 'desativo'
        # o metodo ljust coloca espacos adicionais a direira, ate o valor determinado
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')
    voltar_menu()

def ativar_ou_desativar_restaurante():
    titulo_menu('ativar / desativar restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja ativar / desativar: ')
    # antes de procurar o restaurante, ele ja eh marcado como nao encontrado
    restaurante_encontrado = False
    # percorre toda a lista de restaurantes
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            # caso encontrado, muda a chave para encontrado
            restaurante_encontrado = True
            # o restaurante encontrado recebe o mesmo valor que tinha antes, mas ao contrario
            restaurante['ativo'] = not restaurante['ativo']
            # operador ternario diferenciado: se verdadeiro, condicao, se falso
            mensagem = f'o restaurante restaurante foi ativado com sucesso' if restaurante['ativo'] else f'o restaurante foi desativado com sucesso'
            print(mensagem)
    # caso o restaurante nao foi encontrado, ou seja, continua FALSE mas ao contrario, este IF interpreta como TRUE
    if not restaurante_encontrado:
        print('o restaurante digitado nao foi encontrado')
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaur_ante')
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
            ativar_ou_desativar_restaurante()
        elif opcao_escolhida == 4:
            encerrar_aplicacao()
        else:
            opcao_invalida()
    except Exception as e:
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
import os 

def nome_do_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():

    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def escolher_opcoes():

    valor_escolhido = int (input ('\nEscolha uma opção: '))
    print(f'Você escolheu a opção: {valor_escolhido}')

    ### Se não indicarmos que a variavel valor escolhida não é int, sempre pegar os elses da condições.

    if (valor_escolhido == 1 ):
        print('Cadastrar Restaurante')

    elif (valor_escolhido == 2):
        print('Listar Restaurantes')

    elif(valor_escolhido == 3):
        print('Ativar Restaurante')

    else:
        finalizar_app()

def finalizar_app ():
    os.system('cls')
    print('Encerrando Programa')
    


def main():
    nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    

if __name__ == '__main__':
  main()
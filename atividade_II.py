#Exercicio 1; - Solicite ao usuário que insira um número e, em seguida, 
# use uma estrutura if else para determinar se o número é par ou ímpar.
import os 
def par_impar():
    numero = int (input('Digite um numero: '))

    if numero % 2 == 0 :
        print('O numero Escolhido é um numero PAR')
    else:
        os.system('cls')
        print('O numero Escolhido é IMPAR')

## 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
## Criança: 0 a 12 anos;
## Adolescente: 13 a 18 anos;
## Adulto: acima de 18 anos.


def anos_de_idade():
    idade = int (input('Qual é a sua Idade: '))

    if idade >= 0 and idade <= 12:
        print ('Criança')
    elif idade >= 13 and idade <= 18:
        print('Adolescente')
    else:
        os.system('cls')
        print('Adulto')



def main():
     par_impar()
     anos_de_idade()

if __name__ == '__main__':
       main()






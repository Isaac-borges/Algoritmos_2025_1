# 12. Leia 1 (um) número inteiro e escreva se este número é par ou impar.
from entradas import getInt

def ehPar(num):
    if num % 2 == 0:
        return 'Par'
    else :
        return 'Impar'
    

def main():
    numero = getInt('Número : ')

    classificacao = ehPar(numero)

    print(f'É {classificacao}')

main()
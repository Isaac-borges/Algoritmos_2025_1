# Exercício 3: Verificador de Números Primos
from entradas import getInt

def ehPrimo (num): 
    if (num % 2 != 0) and (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0):
        classif = 'é primo'
    elif (num == 2) or (num == 3) or (num == 5) or (num==7):
        classif = 'é primo' 
    else :
        classif = 'não é primo'

    return classif

def main():
    numero = getInt('Insira um número : ')

    classificacao = ehPrimo(numero)

    print(f'Esse número {classificacao}')

main()
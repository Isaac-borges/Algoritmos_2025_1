# 1. Leia 3 (três) números, verifique e escreva quantos números 
# iguais existem entre os números.

from entradas import getFloat

def conferirIgualdade(n1, n2, n3) :
    if n1 == n2 and n2 == n3 :
        iguais = 3
    elif (n1 == n2 and n2 != n3) or (n1 == n3 and n3 != n2) or (n2 == n3 and n3 != n1):
        iguais = 2
    else :
        iguais = 0
    
    return iguais

def main():
    numero1 = getFloat('Insira um número (1) : ')
    numero2 = getFloat('Insira um número (2) : ')
    numero3 = getFloat('Insira um número (3) : ')

    numIguais = conferirIgualdade(numero1, numero2, numero3)

    print(f'Há {numIguais} números iguais!')

if __name__ == '__main__' :
    main()
    
main()
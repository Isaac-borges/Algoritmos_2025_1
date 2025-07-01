# 9. Leia 1 (um) número entre 0 e 100, verifique e escreva 
# se o número é ou não primo.
from entradas import getIntInRange

def ehPrimo(num) :
    if num == 2 or num == 3 or num == 5 or num == 7 :
        primoORnot = 'é Primo'
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 :
        primoORnot = 'é Primo'
    else : 
        primoORnot = 'não é Primo' 

    return primoORnot

def main():
    numero = getIntInRange('Insira um número entre 1 e 100 : ', 1, 100 )

    primo = ehPrimo(numero)

    print(f'Esse número {primo}!')


main()
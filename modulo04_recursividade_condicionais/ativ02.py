# 2. Leia 2 (dois) números, verifique e escreva o menor 
# e o maior entre os números lidos.
from entradas import getFloat

def maiorORmenor(n1, n2, solicitado):
    if n1 > n2 :
        maior = n1 
        menor = n2
    else : 
        maior = n2
        menor = n1

    if solicitado == 'maior' :
        return maior
    elif solicitado == 'menor' :
        return menor
    

def main():
    numero1 = getFloat('Insira um número (1/2) : ')
    numero2 = getFloat('Insira um número (2/2) : ')

    maior = maiorORmenor(numero1, numero2, 'maior')
    menor = maiorORmenor(numero1, numero2, 'menor')

    print(f'O número {maior} é o maior e {menor} é o menor!')


main()

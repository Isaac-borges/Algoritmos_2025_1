# 5. Leia 3 (três) números e escreva-os em ordem crescente.
from ativ03 import maiorORmeioORmenor
from entradas import getFloat

def main():
    numero1 = getFloat('Insira um número (1/3) : ')
    numero2 = getFloat('Insira um número (2/3) : ')
    numero3 = getFloat('Insira um número (3/3) : ')

    maior = maiorORmeioORmenor(numero1, numero2, numero3, 'maior')
    meio = maiorORmeioORmenor(numero1, numero2, numero3, 'meio')
    menor = maiorORmeioORmenor(numero1, numero2, numero3, 'menor')

    print(f'A ordem crescente destes números é : {menor}, {meio}, {maior}')


main()

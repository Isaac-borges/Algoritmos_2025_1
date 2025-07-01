# 13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. 
# Considere que todos os valores são diferentes.

from utils_int import getInt 

def maximo(num1, num2, num3, num4, num5) :
    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5 :
        maior = num1
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5 :
        maior = num2
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5 :
        maior = num3
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5 :
        maior = num4
    else :
        maior = num5

    return maior

def minimo(num1, num2, num3, num4, num5) :
    if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5 :
        menor = num1
    elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5 :
        menor = num2
    elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5 :
        menor = num3 
    elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5 :
        menor = num4
    else :
        menor = num5

    return menor

def main() :
    num1 = getInt('Escreva um número (1/5) : ') 
    num2 = getInt('Escreva um número diferente (2/5) : ')
    num3 = getInt('Escreva um número diferente (3/5) : ')
    num4 = getInt('Escreva um número diferente (4/5) : ')
    num5 = getInt('Escreva um número diferente (5/5) : ')

    menor = minimo(num1, num2, num3, num4, num5)
    maior = maximo(num1, num2, num3, num4, num5)

    print(f'O maior número é {maior} e o menor é {menor}')

main()
    

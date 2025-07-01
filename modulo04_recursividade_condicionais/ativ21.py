# 21. Realize arredondamentos de números utilizando a regra usual da 
# matemática: se a parte fracionaria for maior do que ou igual a 0,5, 
# o numero é arredondado para o inteiro imediatamente superior, caso 
# contrario, é arredondado para o inteiro imediatamente inferior.
from utils_float import getFloat


def roundNumber(num) :
    parteInteira = num // 1
    parteDecimal = num - parteInteira

    if parteDecimal >= 0.5 :
        parteInteira = parteInteira + 1
    
    return parteInteira


def main():
    numero = getFloat('Insira um número : ')

    arredondamento = roundNumber(numero)

    print(f'O número foi arredondado para {arredondamento}')


main()
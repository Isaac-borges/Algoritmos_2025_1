# 2. Leia N e escreva todos os números inteiros pares de 1 a N.
from utils_int import getPositiveInt

def main() :
    numero = getPositiveInt('Insira um número : ')

    for i in range(1, numero+1, 1):
        if i % 2 == 0 :
            print(i)


main()
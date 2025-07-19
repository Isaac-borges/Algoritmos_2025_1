# 1. Leia N e escreva todos os números inteiros de 1 a N.

from utils_int import getIntMin

def main() :
    teto = getIntMin('Insira um número maior que 1 : ', 2)

    for i in range(1, teto + 1, 1) :
        print(i)


main()
    


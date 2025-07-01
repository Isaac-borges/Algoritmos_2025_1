# 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva 
# os que são maiores que a média.
from utils_int import getInt
def getMedia(soma, qtdNum) :
    return soma/qtdNum

def main() :
    num1 = getInt('Insira um número (1/5) : ')
    num2 = getInt('Insira um número (2/5) : ')
    num3 = getInt('Insira um número (3/5) : ')
    num4 = getInt('Insira um número (4/5) : ')
    num5 = getInt('Insira um número (5/5) : ')

    soma = num1 + num2 + num3 + num4 + num5
    media = getMedia(soma, 5)

    print(f'A média é : {media}')

main()

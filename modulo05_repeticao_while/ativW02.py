from utils_int import getPositiveInt

def getMMC(num1, num2) :
    contador = 1

    while contador % num1 != 0 or contador % num2 != 0 :
        contador += 1
    
    return contador

def main() :
    numero1 = getPositiveInt('Insira um número (1/2) : ')
    numero2 = getPositiveInt('Insira um número (2/2) : ')

    mmc = getMMC(numero1, numero2)

    print(f'O mmc é {mmc}')

main()
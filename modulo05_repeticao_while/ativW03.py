from utils_int import getPositiveInt
def menorEntre2(num1, num2) :
    if num1 <= num2 :
        return num1
    else :
        return num2

def getMDC(num1, num2) :
    contador = menorEntre2(num1, num2)
    print(contador)
    while num1 % contador != 0 or num2 % contador != 0 :
        contador -= 1
    
    return contador

def main() :
    numero1 = getPositiveInt('Insira um número (1/2) : ')
    numero2 = getPositiveInt('Insira um número (2/2) : ')

    mdc = getMDC(numero1, numero2)

    print(f'O mdc é {mdc}')

main()

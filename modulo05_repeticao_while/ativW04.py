from utils_float import getFloatMin

def divisaoPor2Sucessivas(numero) :
    num = numero 

    while num > 1 :
        num /= 2 
    
    return num


def main() :
    numero = getFloatMin('Insira um número : ', 1)

    ultimaDivisao = divisaoPor2Sucessivas(numero)

    print(f'A ultima divisão é {ultimaDivisao}')

main()


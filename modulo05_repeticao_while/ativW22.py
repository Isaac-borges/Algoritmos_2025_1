from utils_int import getInt

def dividir(numero, divisor) :
    quociente = 0
    adicao = 0
    while adicao < numero :
        adicao += divisor
        quociente += 1

    return quociente

def main() :
    numero = getInt('Insira um número : ')
    divisor = getInt('Insira o divisor : ')

    quociente = dividir(numero, divisor)

    print(f'O quociente é {quociente}')

main()
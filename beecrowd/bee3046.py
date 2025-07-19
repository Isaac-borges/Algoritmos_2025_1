def getInt(entrada) :
    numero = input(entrada)

    while True :
        try :
            inteiro = int(numero)
            return inteiro
        except ValueError:
            inteiro = input(entrada)

def getIntInRange(entrada, min, max) :
    numero = getInt(entrada)

    while numero < min or max < numero :
        print('Valor Inválido!')
        numero = getInt(entrada)
    
    return numero

def calcularJogoDuploX(N) :
    numPecas = ((N + 1) * (N + 2)) / 2

    return numPecas

def main() :
    duploX = int(input(''))

    numPecas = calcularJogoDuploX(duploX)
    print(f'{numPecas:.0f}')

main()
def getInt(entrada) :
    numero = input(entrada)

    while True :
        try :
            numero = int(numero)
            return numero
        except ValueError :
            print('Valor inválido')
            numero = input(entrada)

def getIntInRange(entrada, min, max) :
    numero = getInt(entrada) 

    while numero < min or numero > max :
        print('Valor inválido')
        numero = getInt(entrada)
    
    return numero

def parOUimpar(num) :
    if num % 2 == 0 :
        return 'EVEN '
    else :
        return 'ODD '

def positivoOUnegativo(num) :
    if num > 0 :
        return 'POSITIVE'
    else :
        return 'NEGATIVE'

def main() :
    rodadas = getIntInRange('', 0, 10000)

    for i in range(0, rodadas, 1) :
        numero = getIntInRange('', -10000000, 10000000)
        if numero != 0 :
            validacao = parOUimpar(numero)
            validacao += positivoOUnegativo(numero)
        else :
            validacao = 'NULL'

        print(validacao)

main()



def getInt(entrada) :
    numero = input(entrada)
    while True :
        try :
            inteiro = int(numero)
            return inteiro
        except ValueError :
            numero = input(entrada)

def getFloat(entrada) :
    numero = input(entrada)

    while True :
        try :
            real = int(numero)
            return real
        except ValueError :
            numero = input(entrada)

def getIntInRange(entrada, min, max) :
    numero = getInt(entrada)

    while numero > max or numero < min :
        print(f'Digite um número entre {min} e {max} !') 
        numero = getInt(entrada)

    return numero

def getIntMin(entrada, min) :
    numero = getInt(entrada)

    while numero < min :
        print(f'Digite um número maior que {min} !')
        numero = getInt(entrada)

    return numero

def main() : 
    print('Deu errado, é para ter importado uma função!')

if __name__ == '__main__' :
    main()
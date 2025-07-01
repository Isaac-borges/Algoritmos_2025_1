def main():
    pass

def getInt(entrada): 
    numero = input(entrada)
    
    try:
        inteiro = int(numero)
        return inteiro
    except ValueError:
        print('Valor Inválido!')
        return getInt(entrada)


def getFloat(entrada):
    numero = input(entrada)

    try:
        real = float(numero)
        return real
    except ValueError:
        print('Valor Inválido!')
        return getFloat(entrada)


def getIntInRange(entrada, min, max):
    numero = getInt(entrada)

    if numero < min or numero > max :
        print('Valor Inválido!')
        return getIntInRange(entrada, min, max)
    else: 
        return numero


def getNumberMin(entrada, min):
    num = getFloat(entrada)
    if num < min :
        num = getNumberMin(entrada, min)
    
    return num


def getNumberFloor(entrada, min):
    num = getFloat(entrada)
    if num <= min :
        print('Número inválido')
        num = getNumberFloor(entrada, min)
    
    return num


if __name__ == '__main__' :
    main()



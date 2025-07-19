def main():
    pass

def getInt(entrada):
    numero = float(input(entrada))
    #Colocando float para caso a entrada tenha numero decimal, 
    # não parar o programa abruptamente
    
    while numero % 1 != 0 :
        print('Entrada inválida!')
        numero = float(input(entrada))

    return numero



def getFloat(entrada):
    numFloat = float(input(entrada))

    return numFloat


def getNumberInRange(entrada, min, max):
    num = getFloat(entrada)

    if num < min or num > max :
        num = getNumberInRange(entrada, min, max)
    
    return num


def getIntInRange(entrada, min, max):
    num = getFloat(entrada)

    if (num < min or num > max) or (num % 1 != 0)  :
        print('Número inválido!')
        num = getIntInRange(entrada, min, max)
    
    return num

def getNumberMin(entrada, min):
    num = getFloat(entrada)
    if num < min :
        num = getNumberMin(entrada, min)
    
    return num


def getNumberFloor(entrada, min):
    num = getFloat(entrada)
    if num <= min :
        num = getNumberMin(entrada, min)
    
    return num


if __name__ == '__main__' :
    main()



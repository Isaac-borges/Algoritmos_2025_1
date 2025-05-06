def main():
    pass

def getInt(entrada): 
    inteiro = int(input(entrada))
    
    return inteiro


def getFloat(entrada):
    numFloat = float(input(entrada))

    return numFloat


def getNumberInRange(entrada, min, max):
    num = getFloat(entrada)

    if num < min or num > max :
        num = getNumberInRange(entrada, min, max)
    
    return num


def getIntInRange(entrada, min, max):
    num = getInt(entrada)

    if (num < min or num > max) or (num % 1 != 0)  :
        print('Número inválido!')
        num = getNumberInRange(entrada, min, max)
    
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



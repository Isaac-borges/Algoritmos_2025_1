def getFloat(entrada): 
    numero = input(entrada)
    
    try:
        real = float(numero)
        return real
    except ValueError:
        print('Valor Inválido!')
        return getFloat(entrada)
    

def getPositiveFloat(entrada) :
    numero = getFloat(entrada)

    if numero <= 0 :
        print('Digite um número positivo!')
        return getPositiveFloat(entrada)
    else :
        return numero
    

def getNegativeFloat(entrada) :
    numero = getFloat(entrada)

    if numero >= 0 :
        print('Digite um número negativo!')
        return getNegativeFloat(entrada)
    else :
        return numero
    

def getFloatMin(entrada, min) :
    numero = getFloat(entrada)

    if numero < min :
        print(f'Digite um número maior ou igual à {min}!')
        return getFloatMin(entrada, min)
    else:
        return numero
    

def getFloatMax(entrada, max) :
    numero = getFloat(entrada)

    if numero > max :
        print(f'Digite um número menor ou igual à {max}!')
        return getFloatMax(entrada, max)
    else :
        return numero


def getFloatInRange(entrada, min, max) :
    numero = getFloat(entrada)

    if numero < min or numero > max :
        print(f'Digite um número entre {min} e {max}!') 
        return getFloatInRange(entrada, min, max)
    else : 
        return numero


def main() :
    ...


if __name__ == '__main__' :
    main()
    
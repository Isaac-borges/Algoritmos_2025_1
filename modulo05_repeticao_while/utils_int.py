def getInt(entrada): 
    numero = input(entrada)
    
    try:
        inteiro = int(numero)
        return inteiro
    except ValueError:
        print('Valor Inválido!')
        return getInt(entrada)
    

def getPositiveInt(entrada) :
    numero = getInt(entrada)

    if numero <= 0 :
        print('Digite um número positivo!')
        return getPositiveInt(entrada)
    else :
        return numero
    

def getNegativeInt(entrada) :
    numero = getInt(entrada)

    if numero >= 0 :
        print('Digite um número negativo!')
        return getNegativeInt(entrada)
    else :
        return numero
    

def getIntMin(entrada, min) :
    numero = getInt(entrada)

    if numero < min :
        print(f'Digite um número maior ou igual à {min}!')
        return getIntMin(entrada, min)
    else:
        return numero
    

def getIntMax(entrada, max) :
    numero = getInt(entrada)

    if numero > max :
        print(f'Digite um número menor ou igual à {max}!')
        return getIntMax(entrada, max)
    else :
        return numero


def getIntInRange(entrada, min, max) :
    numero = getInt(entrada)

    if numero < min or numero > max :
        print(f'Digite um número entre {min} e {max}!') 
        return getIntInRange(entrada, min, max)
    else :
        return numero


def main() :
    ...


if __name__ == '__main__' :
    main()
    
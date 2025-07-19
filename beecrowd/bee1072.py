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

def main() :
    dentro = 0
    fora = 0
    numeroCasos = getIntInRange('', 0, 10000)
    
    for i in range(0, numeroCasos, 1) :
        num = getIntInRange('', -10000000, 10000000) 

        if num < 10 or num > 20 :
            fora += 1
        else : 
            dentro += 1
    
    print(f'{dentro} in')
    print(f'{fora} out')

main()
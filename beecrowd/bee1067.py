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
    limite = getIntInRange('', 1, 1000)

    for i in range(1, limite+1, 1) :
        if i % 2 != 0 :
            print(i)

main()

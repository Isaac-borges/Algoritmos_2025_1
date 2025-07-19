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
    num = getIntInRange('', 1, 1000) 

    for i in range(1, 11, 1) :
        produto = i * num

        print(f'{i} x {num} = {produto}')

main()

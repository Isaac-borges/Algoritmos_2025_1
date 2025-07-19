def getInt(entrada) :
    numero = input(entrada)

    while True :
        try :
            numero = int(numero)
            return numero
        except ValueError :
            print('Valor inválido')
            numero = input(entrada)

def getPositiveInt(entrada) :
    numero = getInt(entrada) 

    while numero <= 0 :
        print('Valor inválido')
        numero = getInt(entrada)
    
    return numero

def main() :
    limite = getPositiveInt('')
    limite *= 4
    texto = ''

    for i in range(1, limite + 1, 1) :
        if i % 4 != 0 :
            texto += f'{i} '
        else :
            texto += 'PUM'
            print(texto)
            texto = ''       

main()

from entradas import getInt

def numDigitos(numero):
    contador = 1
    quociente = numero //10 

    while quociente != 0: 
        contador += 1
        quociente = quociente // 10
    
    return contador


def main():
    numero = getInt('Num : ')
    num = numDigitos(numero)
    print(num)



main()
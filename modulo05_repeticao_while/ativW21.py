from utils_float import getFloat

def multiplicar(num, vezes) :
    contador = 0 
    produto = 0

    while contador < vezes :
        produto += num
        contador += 1
    
    return produto

def main() :
    numero = getFloat('Insira um número : ')
    vezes = getFloat('Insira a quantidade de vezes : ')

    produto = multiplicar(numero, vezes)

    print(f'O produto é {produto}')

main()
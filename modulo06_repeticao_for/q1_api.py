def mostrarDivisores(T) :
    for i in range(T, 0, -1) :
        if T % i == 0 :
            print(i)

def proximosMultiplos(T) : 
    for i in range(T+1, T+T+1, 1) :
        multiplo = T * i 
        print(f'{i}º multiplo de {T} = {multiplo}')

def main() :
    nome = input('Insira seu nome : ')
    tamanho = len(nome)

    if tamanho % 2 == 0 : 
        proximosMultiplos(tamanho)
    else:
        mostrarDivisores(tamanho)


main()
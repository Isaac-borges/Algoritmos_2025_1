def main():
    nome = input('Nome : ')
    vezes = int(input('Vezes: '))

    escrever(nome, vezes)


def escrever(nome, vezes) :
    contador = 0

    while contador < vezes :
        print(nome)
        contador += 1

main()
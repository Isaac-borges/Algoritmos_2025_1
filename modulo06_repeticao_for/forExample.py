def main() :
    nome = input('Qual seu nome? ')
    qtd = int(input('Quantas vezes? '))

    for i in range(1, qtd+1, 2) :
        print(f'{i} > {nome}')


main()
def media3Numeros(nota1, nota2, nota3, peso1, peso2, peso3) :
    return ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)


def main() :
    rounds = int(input(''))

    for i in range(0, rounds, 1) :
        nota1, nota2, nota3 = input('').split()
        nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)

        media = media3Numeros(nota1, nota2, nota3, 2, 3, 5)
        print(f'{media:.1f}')


main()
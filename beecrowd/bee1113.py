def main() :
    x, y = input('').split()
    x, y = int(x), int(y)

    while x != y :
        print('Crescente' if x < y else 'Decrescente')

        x, y = input('').split()
        x, y = int(x), int(y)

main()
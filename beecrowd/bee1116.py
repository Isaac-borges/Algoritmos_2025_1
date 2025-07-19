def main() :
    rodadas = int(input(''))

    for i in range(0, rodadas, 1) :
        x, y = input('').split()
        
        x = float(x)
        y = float(y)

        if y != 0 :
            divisao = x / y
            print(f'{divisao:.1f}')
        else :
            print('divisao impossivel')

main()

# 6. Escreva a tabuada dos números de 1 a 10.

def main() :
    input('pressione ENTER ... ')

    for i in range(1, 10+1, 1) :
        print('————————————————————————————————')
        for mult in range(1, 10+1, 1) :
            print(f'{i} * {mult} = {i * mult}')
    print('————————————————————————————————')

main()
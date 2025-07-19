def main() :
    num = int(input(''))

    for i in range(1, num+1, 1) :
        if i % 2 == 0 :
            quadrado = i ** 2 

            print(f'{i}^2 = {quadrado}')

main()
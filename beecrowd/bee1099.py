def main() :
    casos = int(input(''))
    for i in range(0, casos, 1) :
        x, y = input('').split()
        x, y = int(x), int(y)
        soma = 0
        teto = x if x >= y else y
        chao = x if x <= y else y
        for i in range(chao+1, teto, 1) :
            if i % 2 != 0 :
                soma += i
        print(soma)

main()
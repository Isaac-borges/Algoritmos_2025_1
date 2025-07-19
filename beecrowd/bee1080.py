def main() :
    maior = -1
    maiorPos = None
    for i in range(1, 101, 1) :
        num = int(input(''))
        if num > maior :
            maior = num
            maiorPos = i
    
    print(maior)
    print(maiorPos)

main()
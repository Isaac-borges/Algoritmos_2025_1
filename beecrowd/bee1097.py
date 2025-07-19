def main() :
    teto = 7
    for i in range(1, 10, 2) :
        for j in range(teto, teto-3, -1) :
            print(f'I={i} J={j}')
        teto += 2

main()
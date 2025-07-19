def main(): 
    tetoJ = 30
    chaoJ = 10
    for i in range(0, 21, 2) :
        for j in range(chaoJ, tetoJ+1, 10) :
            if (i/10) % 1 != 0 and (j/10) % 1 != 0 :
                print(f'I={i/10} J={j/10}')
            else : 
                print(f'I={i/10:.0f} J={j/10:.0f}')
        tetoJ += 2
        chaoJ += 2

main()

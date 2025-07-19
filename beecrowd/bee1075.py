def main() :
    n = int(input(''))

    for i in range(1, 10001, 1) :
        if i % n == 2 :
            print(i)
    
main()
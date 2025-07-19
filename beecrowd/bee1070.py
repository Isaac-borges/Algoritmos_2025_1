def main() :
    num = int(input(''))
    contador = 0

    while contador < 6 : 
        if num % 2 != 0 :
            contador += 1
            print(num)
        
        num += 1

main()
    

def qtdPares(A, B, C, D, E) :
    num = 0 

    if A % 2 == 0 :
        num += 1
    if B % 2 == 0 :
        num += 1
    if C % 2 == 0 :
        num += 1
    if D % 2 == 0 :
        num += 1
    if E % 2 == 0 :
        num += 1
    
    return num

def main() :
    A = int(input(''))
    B = int(input(''))
    C = int(input(''))
    D = int(input(''))
    E = int(input(''))

    qtd = qtdPares(A, B, C, D, E)
    print(f'{qtd} valores pares')

main()

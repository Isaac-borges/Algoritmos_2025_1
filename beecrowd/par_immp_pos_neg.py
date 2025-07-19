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

def qtdImpares(A, B, C, D, E) :
    num = 0 

    if A % 2 != 0 :
        num += 1
    if B % 2 != 0 :
        num += 1
    if C % 2 != 0 :
        num += 1
    if D % 2 != 0 :
        num += 1
    if E % 2 != 0 :
        num += 1
    
    return num

def qtdPositivos(A, B, C, D, E) :
    num = 0 

    if A > 0 :
        num += 1
    if B > 0 :
        num += 1
    if C > 0 :
        num += 1
    if D > 0 :
        num += 1
    if E > 0 :
        num += 1
    
    return num

def qtdNegativos(A, B, C, D, E) :
    num = 0 

    if A < 0 :
        num += 1
    if B < 0 :
        num += 1
    if C < 0 :
        num += 1
    if D < 0 :
        num += 1
    if E < 0 :
        num += 1
    
    return num

def main() :
    A = int(input(''))
    B = int(input(''))
    C = int(input(''))
    D = int(input(''))
    E = int(input(''))

    qtdPar = qtdPares(A, B, C, D, E)
    qtdImpar = qtdImpares(A, B, C, D, E)
    qtdPos = qtdPositivos(A, B, C, D, E)
    qtdNeg = qtdNegativos(A, B, C, D, E)
    print(f'{qtdPar} valor(es) par(es)')
    print(f'{qtdImpar} valor(es) impar(es)')
    print(f'{qtdPos} valor(es) positivo(s)')
    print(f'{qtdNeg} valor(es) negativo(s)')

main()

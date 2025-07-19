def tiparTriangulo(a, b, c) :
    tipoTriangulo = ''
    if a >= (b + c) :
        return 'NAO FORMA TRIANGULO'
    elif a**2 == (b**2 + c**2) :
        tipoTriangulo += 'TRIANGULO RETANGULO'
    elif a**2 > (b**2 + c**2) : 
        tipoTriangulo += 'TRIANGULO OBTUSANGULO'
    elif a**2 < (b**2 + c**2) :
        tipoTriangulo += 'TRIANGULO ACUTANGULO'

    tipoTriangulo2 = ''
    if a == b and b == c :
        tipoTriangulo2 += 'TRIANGULO EQUILATERO'
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a) :
        tipoTriangulo2 += 'TRIANGULO ISOSCELES'
    
    tipoReal = tipoTriangulo + f'\n{tipoTriangulo2}' if tipoTriangulo2 != '' else tipoTriangulo
    return tipoReal

def ordenar(a, b, c): 
    if a == b and b == c :
        maior, meio, menor = a, b, c
    elif a == b and b > c :
        maior, meio, menor = a, b, c
    elif a == c and c > b :
        maior, meio, menor = a, c, b
    elif b == c and c > a :
        maior, meio, menor = b, c, a
    elif b == c and c < a :
        maior, meio, menor = a, c, b
    elif a == c and c < b :
        maior, meio, menor = b, c, a
    elif a == b and b < c :
        maior, meio, menor = c, a, b
    else :
    
        if a > b and a > c :
            maior = a
            if b > c :
                meio = b 
                menor = c
            elif c > b :
                meio = c
                menor = b
        elif b > a and b > c :
            maior = b
            if a > c :
                meio = a
                menor = c
            elif c > a :
                meio = c
                menor = a
            
        elif c > b and c > a :
            maior = c
            if b > a :
                meio = b
                menor = a
            elif a > b :
                meio = a
                menor = b
    
    return maior, meio, menor


def main() :
    a, b, c = input('').split()

    a = float(a)
    b = float(b)
    c = float(c)

    a, b, c = ordenar(a, b, c)
    tipoTriangulo = tiparTriangulo(a, b, c)

    print(tipoTriangulo)

main()
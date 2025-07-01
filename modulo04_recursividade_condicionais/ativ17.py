# 17. Leia valores inteiros em duas variáveis distintas e se o resto da 
# divisão da primeira pela segunda for 1 escreva a soma dessas variáveis 
# mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor 
# são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos 
# pelo primeiro; se for igual a 4 divida a soma dos números lidos pelo segundo, 
# se este for diferente de zero. Em qualquer outra situação escreva o 
# quadrado dos números lidos.

from utils_int import getInt

def main() :
    A = getInt('A : ')
    B = getInt('B : ')
    resto = A % B

    if resto == 1 :
        print(f'A + B + resto = {A + B + resto}')
    elif resto == 2 :
        if A % 2 == 0 and B % 2 == 0 :
            print('A e B são pares')
        elif A % 2 != 0 and B % 2 == 0 :
            print('A é impar e B é par')
        elif A % 2 == 0 and B % 2 != 0 :
            print('A é par e B é impar')
        else :
            print('A e B são impares')
    elif resto == 3 :
        print(f'A * (A + B) = {A * (A*B)}')
    elif resto == 4 :
        print(f'B * (A + B) = {B * (A*B)}')
    else :
        print(f'A² = {A**2} e B² = {B**2}')

main()

    


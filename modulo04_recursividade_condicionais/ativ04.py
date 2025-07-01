# 4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se 
# o algarismo da dezena é igual ou diferente do algarismo da unidade.

from entradas import getIntInRange 

def conferirIgualdade(D, U) :
    if D == U :
        igualdade = 'Iguais'
    else :
        igualdade = 'Diferentes'
        
    return igualdade

def separarDigitos(num, solicitado):
    if solicitado == 'D':
        D = num // 10
        return D
    elif solicitado == 'U':
        U = num % 10
        return U


def main():
    numero = getIntInRange('Insira o número (2 dígitos) : ', 10, 99)

    dezena = separarDigitos(numero, 'D')
    unidade = separarDigitos(numero, 'U')
    igualdade = conferirIgualdade(dezena, unidade)

    print(f'A dezena e a centena são {igualdade}')


main()
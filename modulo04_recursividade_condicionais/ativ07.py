# 7. Leia 3 (três) números (cada número corresponde a um lado do triângulo),
# verifique e escreva se os 3 (três) números formam um triângulo (a soma 
# de dois lados não pode ser menor que o terceiro lado). Se formam, verifique 
# se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) 
# ou escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

from entradas import getNumberFloor

def ehTriangulo(l1, l2, l3) :
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 :
        return True
    else: 
        return False
    

def tiparTriangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3 :
        tipo = 'Equilatero'
    elif (l1 == l2 and l2 != l3) or (l1 == l3 and l3 != l2) or (l2 == l3 and l3 != l1) :
        tipo = 'Isósceles'
    elif l1 != l2 and l1 != l3 and l2 != l3 :
        tipo = 'Escaleno'

    return tipo


def main() :
    lado1 = getNumberFloor('Insira o tamanho do lado (1/3) : ',0)
    lado2 = getNumberFloor('Insira o tamanho do lado (2/3) : ',0)
    lado3 = getNumberFloor('Insira o tamanho do lado (3/3) : ',0)

    if ehTriangulo(lado1, lado2, lado3) : 
        print('É triangulo!')
        tipo = tiparTriangulo(lado1, lado2, lado3)
        print(f'E ele é {tipo}!')
    else: 
        print('Não é triangulo!')


main()
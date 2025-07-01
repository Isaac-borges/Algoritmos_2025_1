# 6. Leia 3 (três) números (cada número corresponde a um ângulo interno
#  do triângulo), verifique e escreva se os 3 (três) números formam
#  um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#  verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo
#  (1 ângulo = 90o) ou obtusângulo (1 ângulo > 90o). Não existe ângulo com
#  tamanho 0o (zero grau).

from entradas import getNumberFloor

def ehTriangulo(a1, a2, a3):
    if a1 + a2 + a3 == 180 :
        return True
    else: 
        return False
    
def tiparTriangulo(a1, a2, a3) :
    if a1 < 90 and a2 < 90 and a3 < 90 :
        tipo = 'Acutângulo'
    elif a1 == 90 or a2 == 90 or a3 == 90 :
        tipo = 'Retângulo'
    elif a1 > 90 or a2 > 90 or a3 > 90 :
        tipo = 'Obtusângulo'

    return tipo


def main():
    angulo1 = getNumberFloor('Insira o ângulo (1/3) : ', 0)
    angulo2 = getNumberFloor('Insira o ângulo (2/3) : ', 0)
    angulo3 = getNumberFloor('Insira o ângulo (3/3) : ', 0)

    if ehTriangulo(angulo1, angulo2, angulo3) :
        print('É um triângulo!')
        tipo = tiparTriangulo(angulo1, angulo2, angulo3) 
        print(f'E ele é {tipo}!')
    else :
        print('Não é triângulo')


main()

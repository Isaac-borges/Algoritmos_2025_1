# Exercício 8: Analisador de Triângulos Avançado
from entradas import getNumberFloor
import math

def perimetroTriangulo(a, b, c) :
    perimetro = a + b + c
    return perimetro 


def getAreaTriangulo(a, b, c, perimetro):
    s = perimetro/2
    area = (s * (s-a) * (s-b) * (s-c))**0.5
    return area 


def ehTriangulo(a, b, c) :
    if a + b > c and a + c > b and b + c > a :
        return True
    else: 
        return False


def tipoTriangulo(a, b, c, criterio) :
    if criterio == 'angulo' :
        Arad = math.acos((b**2 + c**2 - a **2) / (2*b*c))
        Brad = math.acos((a**2 + c**2 - b **2) / (2*a*c))
        Crad = math.acos((a**2 + b**2 - c **2) / (2*a*b))

        anguloA = math.degrees(Arad)
        anguloB = math.degrees(Brad)
        anguloC = math.degrees(Crad)

        if anguloA < 90 and anguloB < 90 and anguloC < 90:
            return 'Acutângulo'
        elif anguloA == 90 or anguloB == 90 or anguloC == 90:
            return 'Retângulo'
        elif anguloA > 90 or anguloB > 90 or anguloC > 90 :
            return 'Obtusângulo'
        

    if criterio == 'comprimento' :
        if a == b and b == c :
            return 'Equilatero'
        elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
            return 'Isosceles'
        else: 
            return 'Escaleno'


def main() :
    ladoA = getNumberFloor('Comprimento do lado A : ', 0)
    ladoB = getNumberFloor('Comprimento do lado B : ', 0)
    ladoC = getNumberFloor('Comprimento do lado C : ', 0)

    perimetro = perimetroTriangulo(ladoA, ladoB, ladoC)
    area = getAreaTriangulo(ladoA, ladoB, ladoC, perimetro)
    verificacao = ehTriangulo(ladoA, ladoB, ladoC)

    if verificacao :
        print('É um triangulo!')
        classAngulo = tipoTriangulo(ladoA, ladoB, ladoC, 'angulo')
        classLado = tipoTriangulo(ladoA, ladoB, ladoC, 'comprimento')

        print(f'O triangulo de lados {ladoA}, {ladoB} e {ladoC} é {classLado} e {classAngulo}')


main()
# 26. Leia os 3 (três) lados de um triângulo e identifique sua 
# hipotenusa e seus catetos.
from utils_float import getPositiveFloat

def main() :
    lado1 = getPositiveFloat('Insira um lado do triangulo (1/3) : ')
    lado2 = getPositiveFloat('Insira um lado do triangulo (2/3) : ')
    lado3 = getPositiveFloat('Insira um lado do triangulo (3/3) : ')
    hipotenusa = 0
    cateto1 = 0
    cateto2 = 0

    if lado1 > lado2 and lado1 > lado3 :
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
    elif lado2 > lado1 and lado2 > lado3 :
        hipotenusa = lado2
        cateto1 = lado1
        cateto2 = lado3
    elif lado3 > lado1 and lado3 > lado2 :
        hipotenusa = lado3
        cateto1 = lado1
        cateto2 = lado2

    print(f'HIPOTENUSA : {hipotenusa} ; CATETOS : {cateto1} e {cateto2}')

main()

    
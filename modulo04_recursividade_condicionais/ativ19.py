# 19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida 
# calcule o índice de massa corpórea (IMC = peso / altura2). Ao final, 
# escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso 
# (IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).
from utils_float import getPositiveFloat

def calcularIMC(h, kg) :
    return kg / h**2

def classificarIMC(imc) :
    if imc < 25 :
        classif = 'NORMAL'
    elif imc <= 30 :
        classif = 'OBESO'
    else :
        classif = 'OBESIDADE MORBIDA'

    return classif
    
def main() :
    peso = getPositiveFloat('Insira seu peso em kg : ')
    altura = getPositiveFloat('Insira sua altura em metros : ')

    imc = calcularIMC(altura, peso)
    classificacao = classificarIMC(imc)

    print(f'Seu imc é : {imc:.2f}')
    print(f'Classificação : {classificacao}')

main()

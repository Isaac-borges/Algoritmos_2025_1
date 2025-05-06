# Exercício 2: Calculadora de IMC com Classificação

from entradas import getFloat

def calcularIMC(peso, altura):
    imc = (peso) / (altura**2)

    return imc

def classificarIMC(imc):
    if imc < 18.5 : 
        classif = 'magreza'
    elif imc <= 24.9 :
        classif = 'normal'
    elif imc <= 29.9 :
        classif = 'sobrepeso'
    elif imc <= 39.9 : 
        classif = 'obesidade'
    else :
        classif = 'obesidade grave'

    return classif

def main() : 
    peso = getFloat('Insira o peso em kg       : ')
    altura = getFloat('Insira a altura em metros : ')

    imc = calcularIMC(peso, altura)
    classificacao = classificarIMC(imc)

    print(f'O seu IMC é {imc:.2f} e sua classificação é {classificacao}')

main()
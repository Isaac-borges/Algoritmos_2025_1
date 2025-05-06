# Exercício 7: Conversor de Temperatura com Validação
from entradas import getNumberMin, getIntInRange

def getTemperatura(escala):
    temperatura = None

    if escala == 1 :
        temperatura = getNumberMin('Temperatura em °C : ', -273.15)
    elif escala == 2 :
        temperatura = getNumberMin('Temperatura em K  : ', 0)
    elif escala == 3 : 
        temperatura = getNumberMin('Temperatura em °F : ', -459.67)

    return temperatura


def convertTemperatura(tempIn, escIn, escCon) :
    tempCon = None
    if escIn == 1 :
        if escCon == 2 :
            tempCon = tempIn + 273.15
        elif escCon == 3 :
            tempCon = (9 * tempIn + 160) / 5

    elif escIn == 2 :
        if escCon == 1 : 
            tempCon = tempIn - 273.15
        elif escCon == 3 :
            tempCon = (tempIn - 273.15) * (9/5) + 32

    elif escIn == 3 : 
        if escCon == 1 : 
            tempCon = (tempIn - 32) * (5/9)
        elif escCon == 2 :
            tempCon = (tempIn - 32) * (5/9) + 273.15


    return tempCon

def getSinalEscala(e):
    sinal = None
    if e == 1 :
        sinal = '°C'
    elif e == 2 :
        sinal = 'K'
    else :
        sinal = '°F'

    return sinal

def main(): 
    print('(Celsius     -> 1)')
    print('(Kelvin      -> 2)')
    print('(Fahrenheir  -> 3)')
    escalaInicial = getIntInRange('Qual escala você vai utilizar?  : ', 1, 3)
    escalaConvert = getIntInRange('Você vai mudar pra qual escala? : ', 1, 3)

    temperatura = getTemperatura(escalaInicial)
    conversao = convertTemperatura(temperatura, escalaInicial, escalaConvert)
    sinalIn = getSinalEscala(escalaInicial)
    sinalCo = getSinalEscala(escalaConvert)

    print(f'A temperatura {temperatura:.2f} {sinalIn} em {sinalCo} é {conversao:.2f} {sinalCo}!')
    
    
main()

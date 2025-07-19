import os

def menu(opcaoMenu):
    if opcaoMenu == 1:
        print('''
    _____________________________________________________________
              BEM VINDO ! 
              PARA COMEÇAR, INFORME SUA SITUAÇÃO ATUAL:
              (RESPONDA CADA UMA NA ORDEM)
              1 - PESO ATUAL
              2 - SEXO (1 - HOMEM; 2 - MULHER)
    _____________________________________________________________
''')
    elif opcaoMenu == 2 :
        print('''
    _____________________________________________________________
              OTIMO ! 
              AGORA SOBRE SUAS EXPECTATIVAS :
              1 - QUANTOS KG QUER PERDER
              2 - QUANTOS DIAS DA SEMANA VOCÊ IRÁ TREINAR
              3 - QUANTAS HORAS POR DIA
              4 - % DO TEMPO IRÁ TREINAR NO TRANSPORT
    _____________________________________________________________ 
''')
        
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def getFloat(entrada) :
    numero = float(input(entrada))

    return numero

def getIntInRange(entrada, floor, ceiling) :
    numero = getFloat(entrada)

    while numero % 1 != 0 or numero < floor or numero > ceiling :
        print('NUMERO INVÁLIDO!')
        numero = getFloat(entrada)

    return numero

def caloriasNecessarias(kgEsperado) :
    return 7000 * kgEsperado

def caloriaPorTransport(percent, dSemana, horas,)

def main():
    conferencia1 = 2
    while conferencia1 != 1 :
        clearScreen()
        menu(1)
        pesoAtual = getFloat('1 > ')
        sexo = getIntInRange('2 > ', 1, 2)
        clearScreen()
        print(f'SEU PESO É {pesoAtual} KG E SEU SEXO É {'MASCULINO' if sexo == 1 else 'FEMININO'}!')
        print('ISSO ESTÁ CERTO? (1 - SIM; 2 - NÃO)')
        conferencia1 = getIntInRange(' > ', 1, 2)

    conferencia2 = 2
    while conferencia2 != 1 :
        clearScreen()
        menu(2)
        kgEsperado = getFloat('1 > ')
        diasSemana = getIntInRange('2 > ', 0, 7)
        horasPdia = getFloat('3 > ')
        percentualTransport = getIntInRange('4 > ', 0, 100)
        percentualEscada = 100 - percentualTransport
        clearScreen()
        print(f'VOCÊ QUER PERDER {kgEsperado} KG, TREINANDO {horasPdia} HORAS POR DIA, EM {diasSemana} DIAS DA SEMANA, TREINANDO {percentualTransport}% DO TEMPO NO TRANSPORT!')
        print('ISSO ESTÁ CERTO? (1 - SIM; 2 - NÃO)')
        conferencia2 = getIntInRange(' > ', 1, 2)
    
    minutos

    caloriasAPerder = caloriasNecessarias(kgEsperado)
    caloriasTransport = caloriaPorTransport(percentualTransport, diasSemana, horasPdia, )
    print('FIM!')


main()
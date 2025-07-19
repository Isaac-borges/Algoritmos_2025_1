import random
import os

def gerarRandom(a, b) :
    return random.randint(a, b)


def gerarSenha(numCaracteres):
    contador = 0
    caractereAnterior = gerarRandom(0, 9)
    caractereAtual = None
    senha = ''

    while contador < numCaracteres :
        caractereAtual = gerarRandom(0, 9)

        if caractereAtual != caractereAnterior + 1 and caractereAtual != caractereAnterior - 1 and caractereAtual != caractereAnterior :
            senha += str(caractereAtual)
            contador += 1
            caractereAnterior = caractereAtual

    return senha



def fileira(caractere, vezes):
    print(caractere * vezes)


def getIntInRange(entrada, floor, ceiling):
    numero = float(input(entrada))

    if numero > ceiling or numero < floor or numero % 1 != 0 :
        print('Numero invalido!')
        numero = getIntInRange(entrada, ceiling, floor)
    
    return numero


def getIntFloor(entrada, floor):
    numero = float(input(entrada))

    if numero < floor or numero % 1 != 0 :
        print('Numero invalido!')
        numero = getIntFloor(entrada, floor)
    
    return numero

def clearScreen():
    os.system('cls')


def menu(exibicao):
    fileira('*', 41)
    print('')
    print(exibicao)
    print('')
    fileira('*', 41)


def main():
    opcao = None 
    while opcao != 0 :
        menu(' Você quer uma senha? (0 - Não, 1 - Sim)')
        opcao = getIntInRange('> ', 0, 1)
        clearScreen()
        while opcao == 1 :
            menu(' Qual o tamanho da senha?')
            tamanho = getIntFloor('> ', 1)
            clearScreen()
            senha = gerarSenha(tamanho)

            menu(f' A sua senha é {senha}, satisfeito? (0 - Parar, 1 - Fazer mais uma) ')
            opcao = getIntInRange('> ', 0, 1)
            clearScreen()
        

    print('FIM!')


main()  
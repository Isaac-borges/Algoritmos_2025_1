# 18. Leia dois valores e uma das seguintes operações a serem executadas
# (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação
# e 4 – Divisão). Calcule e escreva o resultado dessa operação sobre os dois
# valores lidos.
from utils_int import getIntInRange
from utils_float import getFloat

def nomearOperacao(op) :
    if op == 1 :
        nome = 'Adição'
    elif op == 2 :
        nome = 'Subtração'
    elif op == 3 :
        nome = 'Multiplicação'
    else :
        nome = 'Divisão'

    return nome

def main() :
    A = getFloat('Insira um número (1/2) : ')
    B = getFloat('Insira um número (2/2) : ')
    print('Insira a operação desejada')
    print('Opções : ')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    operacao = getIntInRange('> ', 1, 4)
    operacaoNome = nomearOperacao(operacao)

    if operacao == 1 :
        resultado = A + B
    elif operacao == 2 :
        resultado = A - B
    elif operacao == 3 :
        resultado = A * B
    else :
        resultado = A / B if B != 0 else 'Indeterminado'

    print(f'O resultado da {operacaoNome} de {A} e {B} é {resultado}')

main()
    
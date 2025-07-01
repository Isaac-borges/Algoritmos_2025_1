# 8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) 
# de uma pessoa, calcule e escreva sua idade exata (em anos).
from entradas import getInt
def getIdade(dn, mn, an, da, ma, aa) :
    if da >= dn and ma >= mn : 
        idade = aa - an
    else :
        idade = aa - an - 1

    return idade


def main() :
    diaNasc = getInt('Insira dia do nascimento : ')
    mesNasc = getInt('Insira mês do nascimento : ')
    anoNasc = getInt('Insira ano do nascimento : ')
    diaAtual = getInt('Insira dia atual         : ')
    mesAtual = getInt('Insira mês atual         : ')
    anoAtual = getInt('Insira ano atual         : ')

    idade = getIdade(diaNasc, mesNasc, anoNasc, diaAtual, mesAtual, anoAtual)

    print(f'A idade dessa pessoa é   : {idade}')


main()
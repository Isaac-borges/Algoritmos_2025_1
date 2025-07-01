# 27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data 
# (dia, mês e ano) do seu nascimento e a data (dia, mês e ano) atual.
from utils_int import getPositiveInt
def calcularIdade(dA, mA, aA, dN, mN, aN) :
    anos = aA - aN
    meses = mA - mN
    dias = dA - dN

    if mA < mN :  
        anos -= 1
        meses = (mN+12) - mA
    elif mA == mN :
        if dA < dN :
            anos -= 1
            meses = (mN+12) - mA - 1
    
    if dA < dN :
        dias = 30 - (dN - dA)
    
    
    print(f'{anos} anos, {meses} meses e {dias} dias')


def main() :
    diaAtual = getPositiveInt('Dia atual : ')
    mesAtual = getPositiveInt('Mes atual : ')
    anoAtual = getPositiveInt('Ano atual : ')
    diaNasci = getPositiveInt('Dia nascimento : ')
    mesNasci = getPositiveInt('Mes nascimento : ')
    anoNasci = getPositiveInt('Ano nascimento : ')

    calcularIdade(diaAtual, mesAtual, anoAtual, diaNasci, mesNasci, anoNasci)

main()
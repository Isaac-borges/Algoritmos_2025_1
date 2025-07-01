# 23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, 
# mês e ano) e escreva qual delas é a mais recente.
from utils_int import getPositiveInt
from ativ10 import validarData

def conferirRecente(d1, m1, a1, d2, m2, a2) :
    if (a1 > a2) :
        recenteD = d1
        recenteM = m1
        recenteA = a1
    elif (a1 < a2) :
        recenteD = d2
        recenteM = m2
        recenteA = a2
    else :
        if m2 > m1 :
            recenteD = d2
            recenteM = m2
            recenteA = a1
        elif m2 < m1 :
            recenteD = d1
            recenteM = m1
            recenteA = a1
        else :
            if d2 > d1 :
                recenteD = d2
                recenteM = m1
                recenteA = a1
            elif d2 < d1 :
                recenteD = d1
                recenteM = m1
                recenteA = a1
            else: 
                recenteD = d1
                recenteM = m1
                recenteA = a1

    recente = f'{recenteD}/{recenteM}/{recenteA}'
    return recente


def main() :
    dia1 = getPositiveInt('Insira o dia : ')
    mes1 = getPositiveInt('Insira o mes : ')
    ano1 = getPositiveInt('Insira o ano : ')
    dia2 = getPositiveInt('Insira o dia : ')
    mes2 = getPositiveInt('Insira o mes : ')
    ano2 = getPositiveInt('Insira o ano : ')

    if (validarData(dia1, mes1, ano1) == 'inválida' 
        and validarData(dia2, mes2, ano2) == 'inválida') :
        print('Ambas as datas são inválidas!')
    elif (validarData(dia1, mes1, ano1) == 'inválida' 
        and validarData(dia2, mes2, ano2) == 'válida') or (validarData(dia1, mes1, ano1) == 'válida' 
        and validarData(dia2, mes2, ano2) == 'inválida') :
        print('Uma das datas é inválida!')
    else :
        print('Ambas as datas são válidas!')
        recente = conferirRecente(dia1, mes1, ano1, dia2, mes2, ano2)
        print(f'E a data mais recente é {recente}')


main()

        

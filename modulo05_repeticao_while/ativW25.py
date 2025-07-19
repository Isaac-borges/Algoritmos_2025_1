# 25. Foi feita uma pesquisa de audiência de canal de TV em várias casas em Teresina, num certo dia. Para
# cada casa visitada, o entrevistado informou o número do canal (2, 4, 5, 7, 10) e o número de pessoas que
# estavam assistindo TV. Escreva um algoritmo que leia um número indeterminado de dados (terminando
# quando for lido um canal igual a zero) e calcule o percentual de audiência para cada emissora,
# mostrando ao final, o número de cada canal e sua respectiva audiência.

from utils_int import getIntInRange, getPositiveInt

def percentual(parte, total) :
    return (parte / total) * 100

def getCanal(entrada) :
    canal = getIntInRange(entrada, 0, 10)

    while canal != 0 and canal != 2 and canal != 4 and canal != 5 and canal != 7 and canal != 10 :
        print('Canal Inválido!')
        canal = getIntInRange(entrada, 0, 10)

    return canal

def main() :
    canal = getCanal('Qual canal você está assistindo?\n > ')
    total_telespectadores = 0
    cont_2, cont_4, cont_5, cont_7, cont_10 = 0, 0, 0, 0, 0

    while canal != 0 :
        telespectadores = getPositiveInt('Quantas pessoas estão assistindo em sua casa?\n > ')

        total_telespectadores += telespectadores

        if canal == 2 :
            cont_2 += telespectadores
        elif canal == 4 :
            cont_4 += telespectadores
        elif canal == 5 :
            cont_5 += telespectadores
        elif canal == 7 :
            cont_7 += telespectadores
        elif canal == 10 :
            cont_10 += telespectadores
        
        canal = getCanal('Qual canal você está assistindo?\n > ')

    perc_2 = percentual(cont_2, total_telespectadores)
    perc_4 = percentual(cont_4, total_telespectadores)
    perc_5 = percentual(cont_5, total_telespectadores)
    perc_7 = percentual(cont_7, total_telespectadores)
    perc_10 = percentual(cont_10, total_telespectadores)

    relatorio = f'''
RELATORIO DIA X

CANAL 2 = {perc_2:.1f} pontos
CANAL 4 = {perc_4:.1f} pontos
CANAL 5 = {perc_5:.1f} pontos
CANAL 7 = {perc_7:.1f} pontos
CANAL 10 = {perc_10:.1f} pontos

'''
    print(relatorio)

main()
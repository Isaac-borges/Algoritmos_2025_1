# 14. Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
# entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
# responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
# entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
# · a porcentagem de cada candidato;
# · a porcentagem dos outros candidatos;
# · a porcentagem de eleitores indecisos;
# · a porcentagem de votos nulos/brancos;
# · o total de entrevistados;
# · uma mensagem indicando a possibilidade ou não de haver 2o turno.

from utils_int import getIntInRange

def getVoto(entrada) :
    voto = getIntInRange(entrada, -1, 99)

    while voto != -1 and voto != 0 and voto != 13 and voto != 23 and voto != 45 and voto != 98 and voto != 99 :
        print('Opção invalida!')
        voto = getIntInRange(entrada, -1, 99)

    return voto

def percentual(parte, total) :
    return (parte / total) * 100

def main() :
    qtd_opinioes = 0
    nulo = 0
    outros = 0
    indecisos = 0 
    dilma = 0
    serra = 0 
    ciro = 0

    opniao = getVoto('Opnião de voto : ')
    while opniao != -1 :
        qtd_opinioes += 1

        if opniao == 0 :
            nulo += 1
        elif opniao == 13 :
            dilma += 1 
        elif opniao == 23 :
            serra += 1
        elif opniao == 45 :
            ciro += 1
        elif opniao == 98 :
            outros += 1 
        elif opniao == 99 :
            indecisos += 1

        opniao = getVoto('Opnião de voto : ')

    percDilma = percentual(dilma, qtd_opinioes)
    percSerra = percentual(serra, qtd_opinioes)
    percCiro = percentual(ciro, qtd_opinioes)
    percNulo = percentual(nulo, qtd_opinioes)
    percIndecisos = percentual(indecisos, qtd_opinioes)
    percOutros = percentual(outros, qtd_opinioes)

    if percDilma >= 50 or percCiro >= 50 or percSerra >= 50 :
        segundo_turno = 'NÃO'
    else :
        segundo_turno = 'SIM'
    print(f'''
RESULTADO
Total de entrevistados : {qtd_opinioes}

PERCENTUAIS 
Dilma         : {percDilma:.2f} %
Serra         : {percSerra:.2f} %
Ciro          : {percCiro:.2f} %
Outros        : {percOutros:.2f} %
Indecisos     : {percIndecisos:.2f} %
Brancos/Nulos : {percNulo:.2f} %

Segundo Turno : {segundo_turno}   
''')
    
main()
    

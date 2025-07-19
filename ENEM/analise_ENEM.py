from utils_lista import abrirArquivo, listar, mapear
from utils_ENEM import NivelEconomicoPorEstado, adicionarRegiao, formatarSocioEconomico, mediaTotal, mediaTotalPorArea, melhorNaAreaNoEstado, rankingEstado, rankingRegiao, topNbrasil, topNporArea, topNporEstado, topNporEstadoeRede, buscarPorParteNome
from utils_numbers import getIntInRange, getIntMin
from utils_visual import clearScreen, ENTERtoContinue
def menu(opcao_menu) :
    if opcao_menu == 'inicial' :
        print('''
---------------***ENEM***------------------
    1  - Top N Brasil
    2  - Top N Brasil por área
    3  - Top N por Estado
    4  - Top N por Estado e Rede (Publica ou Privada)
    5  - Media Nacional por Área
    6  - Melhor Escola por Área e Estado ou BR
    7  - Lista Escolas por Estado Ordenada Por Renda
    8  - Busca escola específica por parte do nome
    9  - Ranking ENEM por Estado
    10 - Ranking ENEM por Região do País
    
    0 - SAIR
-------------------------------------------''')
    elif opcao_menu == 'estados' :
        print('''
---------------*****ESTADOS*****------------------
    1  - ACRE                    15 - PARAIBA
    2  - ALAGOAS                 16 - PARANÁ
    3  - AMAPA                   17 - PERNAMBUCO
    4  - AMAZONAS                18 - PIAUÍ
    5  - BAHIA                   19 - RIO DE JANEIRO
    6  - CEARÁ                   20 - RIO GRANDE DO NORTE
    7  - DISTRITO FEDERAL        21 - RIO GRANDE DO SUL
    8  - ESPIRITO SANTO          22 - RONDÔNIA
    9  - GOIÁS                   23 - RORAIMA
    10 - MARANHÃO                24 - SANTA CATARINA
    11 - MATO GROSSO             25 - SÃO PAULO
    12 - MATO GROSSO DO SUL      26 - SERGIPE
    13 - MINAS GERAIS            27 - TOCANTINS
    14 - PARÁ                        
-------------------------------------------------''')
    elif opcao_menu == 'areas' : 
        print('''
---------****AREAS****------------
    1 - REDAÇÃO 
    2 - LINGUAGENS
    3 - HUMANAS
    4 - NATUREZA
    5 - EXATAS 
----------------------------------''')
    elif opcao_menu == 'rede' : 
        print('''
---------****AREAS****------------
    1 - MUNICIPAL 
    2 - ESTADUAL
    3 - FEDERAL
    4 - PRIVADA 
----------------------------------''')
    

def main() :
    escolas = abrirArquivo("enem2014_nota_por_escola.txt")
    escolas = mapear(escolas, mediaTotal)
    escolas = adicionarRegiao(escolas)
    escolas = formatarSocioEconomico(escolas)
    opcao = -1 
    # print(escolas[0])
    
    while opcao != 0 :
        clearScreen()
        menu('inicial')
        
        opcao = getIntInRange(' > ', 0, 10)
        clearScreen()
        if opcao == 1 :
            qtd_ranking = getIntMin('Quantas posições? \n > ', 1)
            ranking = topNbrasil(escolas, qtd_ranking)
            listar(ranking)
        elif opcao == 2 :
            menu('areas')
            area = getIntInRange(' > ', 1, 5)
            qtd_ranking = getIntMin('Quantas posições? \n > ', 1)
            ranking = topNporArea(escolas, area, qtd_ranking)
            listar(ranking)
            
        elif opcao == 3 :
            menu('estados')
            estado = getIntInRange(' > ', 1, 27)
            qtd_ranking = getIntMin('Quantas posições? \n > ', 1)
            clearScreen()
            ranking = topNporEstado(escolas, estado, qtd_ranking)
            listar(ranking)
        elif opcao == 4 :
            menu('estados')
            estado = getIntInRange(' > ', 1, 27)
            clearScreen()
            menu('rede')
            rede = getIntInRange(' > ', 1, 4)
            qtd_ranking = getIntMin('Quantas posições? \n > ', 1)
            ranking =  topNporEstadoeRede(escolas, estado, rede, qtd_ranking)
            listar(ranking)
        elif opcao == 5 :
            mediaTotalPorArea(escolas)
        elif opcao == 6 :
            menu('estados')
            estado = getIntInRange('(0 para Brasil) > ', 0, 27)

            clearScreen()
            menu('areas')
            area = getIntInRange(' > ', 1, 5)
            clearScreen()

            melhorNaAreaNoEstado(escolas, estado, area)
        elif opcao == 7 :
            menu('estados')
            estado = getIntInRange(' > ', 1, 27)
            qtd_ranking = getIntMin('Quantas posições? \n > ', 1)
            clearScreen()
            ranking = NivelEconomicoPorEstado(escolas, estado, qtd_ranking)
            listar(ranking)
        elif opcao == 8 :
            trecho = input('Procurar Escola \n > ')
            resultados = buscarPorParteNome(escolas, trecho)
            print('Os resultados são: ')
            listar(resultados)
        elif opcao == 9 :
            ranking = rankingEstado(escolas)
            listar(ranking)
        elif opcao == 10 :
            ranking = rankingRegiao(escolas)
            listar(ranking)

        ENTERtoContinue()
        clearScreen()
    print('FIM!')


main()
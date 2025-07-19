from utils_lista import mapearPosicao, filtrar, reduzir
# Opções --------------------------------------------------------------------------------------------------
def topNbrasil(escolas, max_rank) :
    cesta = sorted(escolas, key=lambda escolas:escolas['media_total'], reverse=True)
    contador = 0

    cesta = mapearPosicao(cesta, rankingGeral, max_rank)
    
    return cesta

def topNporEstado(escolas, estado, max_rank) :
    sigla = EstadoToUF(estado)
    print(sigla)
    cesta = filtrar(escolas, filtrarEstado, sigla)
    print(type(cesta[1]))
    cesta = sorted(cesta, key=lambda escolas:escolas['media_total'], reverse=True)
    
    cesta = mapearPosicao(cesta, rankingGeralEmUF, max_rank)

    return cesta

def topNporArea(escolas, area, max_rank) :
    criterio_area = opcaoToAREA(area)
    cesta = sorted(escolas, key=lambda escolas: escolas[criterio_area], reverse=True)
    nova_cesta = []
    contador = 0 
    for escola in cesta : 
        contador += 1 
        transformado = f'{contador}º > Nome : {escola['nome']}; Média na área : {escola[criterio_area]}'
        nova_cesta.append(transformado)
        if contador == max_rank :
            break
    
    return nova_cesta

def topNporEstadoeRede(escolas, estado, rede, max_rank) :
    sigla = EstadoToUF(estado)
    rede_nome = opcaoToRede(rede)
    print(sigla)
    cesta = filtrar(escolas, filtrarEstado, sigla)
    cesta = filtrar(cesta, filtrarRede, rede_nome)
    cesta = sorted(cesta, key=lambda cesta:cesta['media_total'], reverse=True)
    cesta = mapearPosicao(cesta, rankingEstadoRede, max_rank)

    return cesta

def mediaTotalPorArea(escolas) :
    medias = {}
    for i in range(1, 6, 1) :
        total = 0
        area = opcaoToAREA(i) 
        # print(area)
        for escola in escolas: 
            escola[area] = strToFloat(escola[area])

            total += escola[area]
        
        medias[area] = total / len(escolas)

    print(f'Redação : {medias['redacao']:.2f}\nLinguagens : {medias['linguagens']:.2f}\nHumanas : {medias['humanas']:.2f}\nMatemática : {medias['matematica']:.2f}\nNaturezas : {medias['ciencias_natureza']:.2f}\n ')

def rankingEstado(escolas) :
    estados = []
    for i in range(1, 28, 1) :
        estado = {}
        estado['sigla'] = EstadoToUF(i)
        estados.append(estado)
    
    for estado in estados :
        total = 0
        escolas_estado = filtrar(escolas, filtrarEstado, estado['sigla'])
        for escola in escolas_estado :
            total += float(escola['media_total'])
        
        estado['media_total'] = total / len(escolas_estado)
    
    estados = sorted(estados, key=lambda estados:estados['media_total'], reverse=True)
    estados = mapearPosicao(estados, rankingDosEstados, 27)

    return estados

def rankingRegiao(escolas) :
    regioes = [{'nome' : 'Centro-Oeste'}, {'nome' : 'Nordeste'}, {'nome' : 'Norte'}, {'nome': 'Sul'}, {'nome': 'Sudeste'}]
    for regiao in regioes :
        total = 0
        escolas_regiao = filtrar(escolas, filtrarRegiao, regiao['nome'])
        for escola in escolas_regiao: 
            total += float(escola['media_total'])
        
        regiao['media_total'] = total / len(escolas_regiao)

    regioes = sorted(regioes, key=lambda regioes:regioes['media_total'], reverse=True)
    regioes = mapearPosicao(regioes, rankingRegioes, 5)

    return regioes

def buscarPorParteNome(escolas, nome_parcial) :
    resultado = []

    for escola in escolas :
        nome = escola['nome'].lower()
        if nome_parcial.lower() in nome :
            resultado.append(escola)
        
    resultado = mapearPosicao(resultado, mostrarResultados, len(resultado))

    return resultado

def NivelEconomicoPorEstado(escolas, num_estado, max_rank) :
    sigla = EstadoToUF(num_estado)
    escolas_estado = filtrar(escolas, filtrarEstado, sigla)
    for escola in escolas_estado :
        escola['nivel_economico_ordem'] = nivelToOrdem(escola['nivel_socio_economico'])
    
    escolas_estado = sorted(escolas_estado, key=lambda escolas_estado:escolas_estado['nivel_economico_ordem'], reverse=False)
    escolas_estado = mapearPosicao(escolas_estado, OrdemNivelEconomico, max_rank)

    return escolas_estado

def melhorNaAreaNoEstado(escolas, num_estado, num_area) :
    sigla = EstadoToUF(num_estado)
    nome_area = opcaoToAREA(num_area)

    if num_estado != 0 :
        escolas_estado = filtrar(escolas, filtrarEstado, sigla)
    else :
        escolas_estado = escolas
    
    escolas_estado = sorted(escolas_estado, key=lambda escolas_estado:escolas_estado[nome_area], reverse=True)
    contador = 0

    for item in escolas_estado :
        print(f'Escola que melhor desempenho na área escolhida no {item['uf']} : {item['nome']}.\nMédia na área : {item[nome_area]}')
        contador += 1
        if contador == 1 :
            break


#dicionarios -----------------------------------------------------------------------------------------------------------

def opcaoToAREA(num_area) :
    dicionario = {
        1 : 'redacao',
        2 : 'linguagens',
        3 : 'humanas', 
        4 : 'ciencias_natureza', 
        5 : 'matematica'
    }

    return dicionario.get(num_area, '')

def opcaoToRede(num_rede) :
    dicionario = {
        1 : 'Estadual',
        2 : 'Municipal',
        3 : 'Federal',
        4 : 'Privada'
    }

    return dicionario.get(num_rede, 'Não Informado')

def EstadoToUF(num_UF) :
    dicionario = {
        1 : 'AC',
        2 : 'AL',
        3 : 'AP',
        4 : 'AM',
        5 : 'BA',
        6 : 'CE',
        7 : 'DF',
        8 : 'ES',
        9 : 'GO',
        10 : 'MA',
        11 : 'MT',
        12 : 'MS',
        13 : 'MG',
        14 : 'PA',
        15 : 'PB',
        16 : 'PR',
        17 : 'PE',
        18 : 'PI',
        19 : 'RJ',
        20 : 'RN',
        21 : 'RS',
        22 : 'RO',
        23 : 'RR',
        24 : 'SC',
        25 : 'SP',
        26 : 'SE',
        27 : 'TO'
    }

    return dicionario.get(num_UF, 'BR')

def UFtoRegiao(UF) :
    dicionario = {
        'AC' : 'Norte',
        'AL' : 'Nordeste',
        'AP' : 'Norte',
        'AM' : 'Norte',
        'BA' : 'Nordeste',
        'CE' : 'Nordeste',
        'DF' : 'Centro-Oeste',
        'ES' : 'Sudeste',
        'GO' : 'Centro-Oeste',
        'MA' : 'Nordeste',
        'MT' : 'Centro-Oeste',
        'MS' : 'Centro-Oeste',
        'MG' : 'Sudeste',
        'PA' : 'Norte',
        'PB' : 'Nordeste',
        'PR' : 'Sul',
        'PE' : 'Nordeste',
        'PI' : 'Nordeste',
        'RJ' : 'Sudeste',
        'RN' : 'Nordeste',
        'RS' : 'Sul',
        'RO' : 'Norte',
        'RR' : 'Norte',
        'SC' : 'Sul',
        'SP' : 'Sudeste',
        'SE' : 'Nordeste',
        'TO' : 'Norte'
    }

    return dicionario.get(UF, 'Brasil')

def nivelToOrdem(nivel) :
    dicionario = {
        'Muito Alto' : '1',
        'Alto' : '2',
        'Medio Alto' : '3',
        'Medio' : '4',
        'Medio Baixo' : '5',
        'Baixo' : '6',
        'Muito Baixo' : '7',
    }

    return dicionario.get(nivel, '8')

# Funções map, filter, reduce------------------------------------------------------------------------------
def rankingGeral(escola, pos_atual) :
    return f'{pos_atual}º > Nome : {escola['nome']}; Média Geral : {escola['media_total']}'

def rankingGeralEmUF(escola, pos_atual) :
    return f'{pos_atual}º em {escola['uf']} > Nome : {escola['nome']}; Média Geral : {escola['media_total']}'

# def rankingGeralEmArea(escola, pos_atual) :
#     return f'{pos_atual}º > Nome : {escola['nome']}; Média Geral : {escola['media_total']}'

def rankingEstadoRede(escola, pos_atual) :
    return f'{pos_atual}º em {escola['uf']} > Nome : {escola['nome']}; Média Geral : {escola['media_total']}; Rede: {escola['rede']}'

def porMediaGeral(escolas) :
    return escolas['media_total']

def porArea(escola, criterio_area) :
    return escola[criterio_area]

def somarMedias(item, estado_anterior) :
    return float(item['media_total']) + estado_anterior

def filtrarEstado(item, sigla) :  
    return item['uf'] == sigla

def filtrarRegiao(item, regiao) :  
    return item['regiao'] == regiao

def filtrarRede(item, rede) :
    return item['rede'] == rede

def mostrarResultados(item, pos_atual) :
    return f' - {item['nome']}; Rede: {item['rede']}, {item['municipio']}-{item['uf']}. Média no ENEM: {item['media_total']}'

def OrdemNivelEconomico(item, pos_atual) :
    return f'Nome da escola : {item['nome']}; Nível Socio-Econômico : {item['nivel_socio_economico']}. Média no ENEM: {item['media_total']}'

def rankingDosEstados(item, pos_atual) :
    return f'{pos_atual}º > Estado : {item['sigla']}; Média : {item['media_total']:.2f}'

def rankingRegioes(item, pos_atual) :
    return f'{pos_atual}º > Região : {item['nome']}; Média : {item['media_total']:.2f}'

# Outros ---------------------------------------------------------------------------------------------------
def mediaTotal(escola) :
    novo_item = escola
    parte_inteira, parte_decimal = escola['media_objetivas'].split(',')
    parte_inteira, parte_decimal = float(parte_inteira), float(parte_decimal) / 100
    media_objetiva = parte_inteira + parte_decimal

    parte_inteira, parte_decimal = escola['redacao'].split(',')
    parte_inteira, parte_decimal = float(parte_inteira), float(parte_decimal) / 100
    media_redacao = parte_inteira + parte_decimal
    media_objetivas_redacao = (media_objetiva + media_redacao) / 2
    novo_item['media_total'] = f'{media_objetivas_redacao:.2f}'

    return novo_item

def formatarSocioEconomico(escolas) :
    cesta = escolas 
    for escola in cesta : 
        if escola['nivel_socio_economico'] == 'M�dio Baixo' :
            escola['nivel_socio_economico'] = 'Medio Baixo' 
        elif escola['nivel_socio_economico'] == 'Sem informa��o':
            escola['nivel_socio_economico'] = 'Sem informacao' 
        elif escola['nivel_socio_economico'] == 'M�dio Alto':
            escola['nivel_socio_economico'] = 'Medio Alto'
        elif escola['nivel_socio_economico'] == 'M�dio' :
            escola['nivel_socio_economico'] = 'Medio'
    
    return cesta

def strToFloat(numero) :
    parte_inteira, parte_decimal = numero.split(',') 
    parte_inteira, parte_decimal = float(parte_inteira), float(parte_decimal) / 100
    # print(parte_decimal, parte_decimal)
    return parte_inteira + parte_decimal

def adicionarRegiao(escolas) :
    cesta = escolas
    for escola in cesta :
        uf = escola['uf']
        escola['regiao'] = UFtoRegiao(uf)
    
    return cesta
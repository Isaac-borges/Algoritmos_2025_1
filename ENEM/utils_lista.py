def abrirArquivo(nome_arquivo) :
    arquivo = open(nome_arquivo)
    cesta = []
    for linha in arquivo :
        dados = linha.strip('\n')
        escola = {}
        ranking, escola['nome'], escola['municipio'], escola['uf'], escola['rede'], escola['permanencia'], escola['nivel_socio_economico'], escola['media_objetivas'], escola['linguagens'], escola['matematica'], escola['ciencias_natureza'], escola['humanas'], escola['redacao'] = dados.split(';')
        cesta.append(escola)

    return cesta

def listar(cesta) :
    for item in cesta : 
        print(item)

def filtrar(colecao, funcao_criterio, criterio) :
    cesta = []

    for item in colecao :
        if funcao_criterio(item, criterio) :
            cesta.append(item)
    
    return cesta

def mapear(colecao, funcao_mapeadora) :
    cesta = []

    for item in colecao :
        item_transformado = funcao_mapeadora(item)
        cesta.append(item_transformado)
    
    return cesta

def mapearPosicao(colecao, funcao_mapeadora, ultima_pos) :
    cesta = [] 
    pos_atual = 0
    for item in colecao :
        pos_atual += 1
        item_transfomado = funcao_mapeadora(item, pos_atual)
        cesta.append(item_transfomado)

        if pos_atual == ultima_pos :
            break

    return cesta

def reduzir(colecao, funcao_redutora, valor_inicial) :
    acumulado = valor_inicial

    for item in colecao :
        acumulado = funcao_redutora(item, acumulado)

    return acumulado

def main() :
    pass

if __name__ == '__main__' :
    main()


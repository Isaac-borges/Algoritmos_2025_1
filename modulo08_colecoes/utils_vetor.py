def filtrar(colecao, funcao_criterio) :
    cesta = []

    for item in colecao :
        if funcao_criterio(item) :
            cesta.append(item)

    return cesta

def filtrarNumerosEspecificos(colecao, numero) :
    cesta = []

    for item in colecao :
        if item != numero:
            cesta.append(item)
    
    return cesta

def removerPorPosicao(colecao, posicao) :
    cesta = []
    contador = 0

    for numero in colecao :
        if contador != posicao - 1 :
            cesta.append(numero)

        contador += 1
    
    return cesta

def mapear(colecao, funcao_transformadora) :
    cesta = []

    for item in colecao :
        item_transformado = funcao_transformadora(item)
        cesta.append(item_transformado)

    return cesta

def reducao(colecao, funcao_redutora, valor_inicial) :
    acumulado = valor_inicial

    for item in colecao :
        acumulado = funcao_redutora(acumulado, item)

    return acumulado

def main() :
    pass

if __name__ == '__main__' :
    main()

def adicionar(item, adicionador ) :
    return item + adicionador

def getMaiorPosicao(colecao) :
    maior = colecao[0]
    maiorpos = 1
    posicao = 0
    for numero in colecao :
        posicao += 1
        if numero > maior :
            maior = numero
            maiorpos = posicao
    
    return [maior, maiorpos]

def getMenorPosicao(colecao) :
    menor = colecao[0]
    menorpos = 1
    posicao = 0
    for numero in colecao :
        posicao += 1
        if numero < menor :
            menor = numero
            menorpos = posicao
    
    return [menor, menorpos]
    
def editarPosicao(vetor, posicao, valor) :
    novo_vetor = vetor 
    novo_vetor[posicao - 1] = valor

    return novo_vetor
def getInt(entrada) :
    numero = input(entrada)

    while True :
        try :
            inteiro = int(numero)
            return inteiro
        except ValueError:
            inteiro = input(entrada)

def getIntInRange(entrada, min, max) :
    numero = getInt(entrada)

    while numero < min or max < numero :
        print('Valor Inválido!')
        numero = getInt(entrada)
    
    return numero

def criarPredios(numPredios, listaAndares):
    representacaoPredios = ''
    for i in range(0, numPredios, 1) :
        representacaoPredios += f"{('*' * (listaAndares[i] + 1))}\n" if i != (numPredios - 1) else f"{('*' * (listaAndares[i] + 1))}"
    
    return representacaoPredios

def calcularMaiorDistancia(predios, tamanho) :
    tamanhoComparacao = tamanho
    allDistancias = []
    for i in range(0, tamanho, 1) :
        predio = predios.split()[i]
        tamanho = len(predio)
        for j in range(0, tamanhoComparacao, 1) :
            comparacao = predios.split()[j]
            if j == i - 1 or j == i + 1 :
                allDistancias.append((len(predio) + len(comparacao) - 1))
            elif i == j :
                pass
            else :
                indexes = (i, j)
                maiorIndex = max(indexes)
                menorIndex = min(indexes)
                allDistancias.append(len(predio) + len(comparacao) + (maiorIndex - menorIndex - 1) - 1)
            
            print(allDistancias)
            
    maiorDistancia = max(allDistancias)

    return maiorDistancia

def pedirItensIntInRange(entrada, min, max, quantidade) :
    itens = input(entrada)
    cesta = []
    try: 
        for i in range(0, quantidade, 1) :
            numero = int(itens.split()[i])
            cesta.append(numero)
    except IndexError:
        return pedirItensIntInRange(entrada, min, max, quantidade)
    except ValueError:
        return pedirItensIntInRange(entrada, min, max, quantidade)

    return cesta

def main() :
    numPredios = getIntInRange('', 2, 200000)
    cestaAndares = pedirItensIntInRange('', 1, 1000000000, numPredios)
    
    predios = criarPredios(numPredios, cestaAndares)
    maiorDistancia = calcularMaiorDistancia(predios, numPredios)
    print(maiorDistancia)

main()

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

def numMaximoInLista(lista) :
    for numero in lista :
        if conferirTodosMaior(numero, lista) :
            maior = numero

    return maior

def conferirTodosMaior(num, lista) :
    for i in lista :
        if ehMenor(num, i) :
            return False
        
    return True

def ehMenor(num, comparacao) :
    if num >= comparacao :
        return False
    
    return True

def calcularMaiorDistancia(predios, tamanho, prediosNum) :
    tamanhoComparacao = tamanho
    allDistancias = []
    mudancasArray = 0
    for i in range(0, tamanho, 1) :
        predio = predios.split()[i]
        predioLen = len(predios.split()[i])
        if predioLen == (max(prediosNum)+1) :
            print('sim')
            for j in range(0, tamanhoComparacao, 1) :
                comparacao = predios.split()[j]
                print(f'---- {j} ----')
                if j == i - 1 or j == i + 1 :
                    allDistancias.append((len(predio) + len(comparacao) - 1))
                elif i == j :
                    pass
                else :
                    indexes = (i, j)
                    maiorIndex = max(indexes)
                    menorIndex = min(indexes)
                    allDistancias.append(len(predio) + len(comparacao) + (maiorIndex - menorIndex - 1) - 1)
                mudancasArray += 1
                print(allDistancias)
    print(mudancasArray)
    print(max(allDistancias))
            


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
    calcularMaiorDistancia(predios, numPredios, cestaAndares)
    

main()

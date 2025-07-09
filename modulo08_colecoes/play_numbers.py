from utils_int import getIntInRange, getIntMin, getPositiveInt
from utils_visual import enterToContinue, clearScreen
from utils_float import getFloat, getFloatInRange, getPositiveFloat, getFloatMin
from utils_vetor import editarPosicao, mapear, filtrar, reducao, getMaiorPosicao, getMenorPosicao, filtrarNumerosEspecificos, removerPorPosicao
from utils_string import getNomeArquivo
import random

def menu(nome_tela) :
    if nome_tela == 'inicial' :
        print('''
-------------------------------------
           PLAY NUMBERS 
    1 - Inicializar vetores (Apenas com vetor vazio)
    2 - Mostrar valores
    3 - Resetar Vetor
    4 - Quantidade de itens no vetor
    5 - Maior e menor número com posição
    6 - Somatório dos valores
    7 - Média dos valores
    8 - Números positivos e quantidade
    9 - Números negativos e quantidade
    10 - Atualização de todos os valores
    11 - Adicionar novos valores
    12 - Remover itens por valor exato
    13 - Remover por posição
    14 - Editar por posição
    15 - Salvar valores em arquivo
    16 - Sair
-------------------------------------''')
    elif nome_tela == 'vetores' :
        print('''
-------------------------------------
          OPÇÕES DE VETORES
    1 - DADOS AUTOMÁTICOS
    2 - INFORMAR VALORES
    3 - VALORES DE UM ARQUIVO
-------------------------------------''')
    elif nome_tela == 'regras' :
        print('''
-------------------------------------
        REGRAS DE ATUALIZAÇÃO
    1 - Multiplicar por valor
    2 - Elevar por valor
    3 - Reduzir à fração
    4 - Substituir valores negativos
    5 - Ordenar valores
    6 - Embaralhar valores
-------------------------------------''')


# Geração do Vetor
def inicializarVetor() :
    qtd_num_vetor = getPositiveInt('Quantidade de números no vetor : \n > ')
    minimo = getFloat('Valor mínimo do vetor : \n > ')
    maximo = getFloat('Valor máximo do vetor : \n > ')
    clearScreen()
    menu('vetores')
    opcao = getIntInRange(' > ', 1, 3)
    if opcao == 1 :
        casas_decimais = getIntMin(' Quantas casas decimais? > ', 0)
        vetor = gerarAleatoriosInRange(qtd_num_vetor, minimo, maximo, casas_decimais)
    elif opcao == 2 :
        vetor = informarValoresInRange(qtd_num_vetor, minimo, maximo)
    else :
        while True :
            try :
                nome_arquivo = input(' Nome ou caminho relativo do arquivo (break = 0) > ') 
                if nome_arquivo == '0' :
                    vetor = []
                    break
                vetor = abrirArquivoComVetor(nome_arquivo, qtd_num_vetor, minimo, maximo)
                return vetor
            except FileNotFoundError :
                print('Insira um nome de arquivo válido!')
                
    return vetor

def gerarAleatoriosInRange(tamanho_vetor, min, max, casas_decimais) :
    cesta = []

    for i in range(0, tamanho_vetor, 1) :
        numero = round(random.uniform(min, max), casas_decimais)
        cesta.append(numero)

    return cesta

def informarValoresInRange(tamanho, min, max) :
    cesta = []
    for i in range(0, tamanho, 1) :
        numero = getFloatInRange(' > ', min, max)
        cesta.append(numero)
    
    return cesta

def abrirArquivoComVetor(nome_arquivo, tamanho, min, max) :
    cesta = []
    arquivo = open(nome_arquivo, encoding="utf8")

    for linha in arquivo :
        numero = linha.strip()
        try :
            numero = float(numero)
            if numero >= min and numero <= max :
                cesta.append(numero)
        except ValueError :
            continue

        if len(cesta) == tamanho :
            break
    
    return cesta

# Listar vetor
def listarVetor(vetor) :
    for numero in vetor :
        print(numero)

#Auxiliares Map, filter e Reduce
def adicionarRedutor(acumulado, item) :
    return acumulado + item

def filterPositivos(item) :
    return item > 0

def filterNegativos(item) :
    return item < 0

def mapearMatematico(colecao, funcao_matematica, razao) :
    cesta = []

    for item in colecao :
        item_transformado = funcao_matematica(item, razao)
        cesta.append(item_transformado)
    
    return cesta

def multiplicarMap(item, razao) :
    return item * razao

def elevarMap(item, razao) :
    return item ** razao

def fracaoMap(item, fracao) :
    return (item*fracao[0]) / fracao [1]

def substituirInRange(item, minmax) :
    return round(random.uniform(minmax[0], minmax[1]), 2) if item < 0 else item

# Atualizações 
def atualizarValores(colecao) :
    vetor = colecao
    menu('regras')
    opcao = getIntInRange(' > ', 1, 6) 
    clearScreen()
    if opcao == 1 :
        multiplicador = getFloat(' Insira o valor pra multiplicar os itens do vetor > ')
        vetor = mapearMatematico(vetor, multiplicarMap, multiplicador)
    elif opcao == 2 :
        elevador = getFloat(' Insira o valor pra elevar os itens do vetor > ')
        vetor = mapearMatematico(vetor, elevarMap, elevador)
    elif opcao == 3 :
        numerador, denominador = input(' Digite uma fração (exemplo 1/5) > ').split('/')
        numerador, denominador = float(numerador), float(denominador)
        fracao = [numerador, denominador]
        vetor = mapearMatematico(vetor, fracaoMap, fracao)
    elif opcao == 4 :
        minimo = getFloat(' Insira um valor mínimo para a substituição > ')
        maximo = getFloatMin(' Insira um valor máximo para a substituição > ', minimo)
        minmax = [minimo, maximo]
        vetor = mapearMatematico(vetor, substituirInRange, minmax)
    elif opcao == 5 :
        reverso = getIntInRange(' A ordenação será reversa ? \n (1 - SIM) \n (2 - NÃO) \n > ', 1, 2)
        vetor = sorted(vetor, reverse=True if reverso == 1 else False)
    else :
        random.shuffle(vetor)
    
    return vetor

def adicionarValores(colecao) :
    vetor = colecao
    num_valores = getIntMin('Quantos valores adicionar? > ', 0)

    for i in range(0, num_valores, 1) :
        valor = getFloat('Valor: ')
        vetor.append(valor)

    return vetor



def salvarVetor(vetor, nomearquivo) :
    with open(nomearquivo, 'w') as arquivo :
        for numero in vetor :
            arquivo.write(f'{numero}\n')

def main() :
    clearScreen()
    vetor = []
    opcao = -1

    while opcao != 16 :
        menu('inicial')
        opcao = getIntInRange(' > ', 1, 16)
        clearScreen()

        if opcao == 1 :
            if vetor == [] :
                vetor = inicializarVetor()
            else :
                print('Um vetor já existe!')  
        elif opcao == 2 :
            listarVetor(vetor)
        elif opcao == 3 :
            vetor = []
            print('Vetor esvaziado!')
        elif opcao == 4 :
            tamanho_vetor = len(vetor)
            print(f'O vetor tem {tamanho_vetor} números!' if tamanho_vetor > 0 else 'Vetor vazio!')
        elif opcao == 5 :
            menor = getMenorPosicao(vetor)
            maior = getMaiorPosicao(vetor)

            print(f'MAIOR NÚMERO = {maior[0]}; POSIÇÃO : {maior[1]}')
            print(f'MENOR NÚMERO = {menor[0]}; POSIÇÃO : {menor[1]}')
        elif opcao == 6 :
            somatorio = reducao(vetor, adicionarRedutor, 0)
            print(f'O somatório dos números do vetor é {somatorio}')
        elif opcao == 7 :
            media = reducao(vetor, adicionarRedutor, 0) / len(vetor)
            print(f'A média do vetor é {media:.2f}')
        elif opcao == 8 :
            numeros_positivos = filtrar(vetor, filterPositivos)
            qtd_positivos = len(numeros_positivos)
            print(f'Temos {qtd_positivos} números positivos, e eles são : ')
            listarVetor(numeros_positivos)
        elif opcao == 9 :
            numeros_negativos = filtrar(vetor, filterNegativos) 
            qtd_negativos = len(numeros_negativos)
            print(f'Temos {qtd_negativos} números negativos, e eles são : ')
            listarVetor(numeros_negativos)
        elif opcao == 10 :
            vetor = atualizarValores(vetor)
        elif opcao == 11 :
            vetor = adicionarValores(vetor)
        elif opcao == 12 :
            numero_a_remover = getFloat(' Qual número será removido? > ')
            vetor = filtrarNumerosEspecificos(vetor, numero_a_remover)
        elif opcao == 13 :
            posicao_a_remover = getPositiveInt('Qual posição você vai remover ? > ')
            vetor = removerPorPosicao(vetor, posicao_a_remover)
        elif opcao == 14 :
            tamanho_vetor = len(vetor)
            posicao_a_editar = getIntInRange('Qual posição você vai editar ? > ', 1, tamanho_vetor)
            valor_da_posicao = getFloat('Edite o valor da posição escolhida > ')
            vetor = editarPosicao(vetor, posicao_a_editar, valor_da_posicao) 
        elif opcao == 15 :
            nome_arquivo = getNomeArquivo(' Nome do arquivo (sem extensão do arquivo, como .txt) > ')
            salvarVetor(vetor, nome_arquivo) 
    
        enterToContinue()
        clearScreen()
    salvarVetor(vetor, 'lista_de_numeros.txt') 
    print('Valores salvos automáticamente em "lista_de_numeros.txt"! \nFIM!')


main()

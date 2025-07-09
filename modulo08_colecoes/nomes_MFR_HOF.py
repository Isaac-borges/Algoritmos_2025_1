import os

# map, filter, reduce

def filtrar(colecao, funcao_criterio) :
    cesta = []
    for item in colecao :
        if funcao_criterio(item) :
            cesta.append(item)
    
    return cesta

def mapear(colecao, funcao_mapeadora) :
    pass

def reduzir(colecao, funcao_redutora, valor_inicial) :
    acumulado = valor_inicial

    for item in colecao :
        acumulado = funcao_redutora(acumulado, item)

# Auxiliares
def nomesTamanhoImpar(nome) :
    return len(nome) % 2 != 0

def contarCaracteresRedutora(acumulado, item) :
    return acumulado + contarCaractere(item)

def contarCaractere(item) :
    return len(item)

 
def menu() :
    print('''
Brincadeira de nomes
          
1 - Add Nome
2 - List Nomes
3 - List Nomes in Arquivos
4 - Nomes com tamanho impar
5 -

''')
    
def listarNomes(nomes) :
    for nome in nomes :
        print(nome)
    
def abrirArquivo(nome_arquivo: str) :
    arquivo = open(nome_arquivo)
    colecao = []
    for palavra in arquivo :
        nome = palavra.strip()
        colecao.append(nome)

    return colecao

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')
    

def main() :
    listaNomes = []
    opcao = -1

    while opcao != 0 :
        clearScreen()
        menu()
        listaNomes = abrirArquivo('/Users/Isaac Borges/OneDrive/Desktop/Algoritmos_2025_1/modulo08_colecoes/listaDeNomes.txt')
        opcao = int(input(' > '))
        clearScreen()
        if opcao == 1 :
            nome = input('Nome : ')
            listaNomes.append(nome)
        if opcao == 2 :
            listarNomes(listaNomes)
        if opcao == 4 :
            nomesFiltrados = filtrar(listaNomes, nomesTamanhoImpar)
            listarNomes(nomesFiltrados)

        input('ENTER to continue ...')

main()
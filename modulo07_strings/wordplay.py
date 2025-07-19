from utils_visual import enterToContinue, clearScreen
from utils_int import getIntInRange, getIntMin
from utils_string import getTextMin, contem_caracter, has_no_word, contem_proibidas, uses_only, uses_all, is_abecedarian 

def menu() :
    print('''
------------------------------------------------------------------
                            WORDPLAY
        1 - Mostrar todas as palavras
        2 - Palavras com no mínimo N caracteres
        3 - Palavras sem 'e'
        4 - Palavras sem letras proibidas
        5 - Palavras com apenas letras indicadas
        6 - Palavras que utilizam todas as letras indicadas
        7 - Palavras com letras em ordem alfabética
          
------------------------------------------------------------------
''')
    
def mostrarTudo() :
    arquivo = open('br-sem-acentos.txt')
    contador = 0

    for linha in arquivo :
        contador += 1
        palavra = linha.strip()
        print(palavra)

    print(f'O total de palavras é {contador}')

def mostrarMinimoCaracteres() :
    minimoCaracteres = getIntMin('Insira o mínimo de caracteres : ', 1)

    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalMinimos = 0

    for linha in arquivo :
        totalPalavras +=1
        palavra = linha.strip()
        if len(palavra) >= minimoCaracteres :
            totalMinimos += 1
            print(palavra)

    print(f'De {totalPalavras} palavras, {totalMinimos} palavras tem pelo menos {minimoCaracteres} caracteres!')

def palavrasSemE() :
    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalSemE = 0
    for linha in arquivo : 
        totalPalavras += 1
        palavra = linha.strip()

        verificacao = has_no_word(palavra, 'e')
        if verificacao == True:
            totalSemE += 1
            print(palavra)

    print(f'De {totalPalavras} palavras, {totalSemE} não possuem E')

def letrasProibidas() :
    letrasProibidas = getTextMin('Insira letras proibidas : ', 1)
    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalSemProibidas = 0

    for linha in arquivo :
        palavra = linha.strip()
        totalPalavras += 1
        
        verificacao = contem_proibidas(palavra, letrasProibidas)
        if verificacao == False:
            totalSemProibidas += 1
            print(palavra)

    print(f'De {totalPalavras} palavras, {totalSemProibidas} não possuem letras Proibidas')


def letrasIndicadas() :
    letrasIndicadas = getTextMin('Insira letras para Analise : ', 1)
    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalComIndicadas = 0

    for linha in arquivo :
        palavra = linha.strip()
        totalPalavras += 1
        
        verificacao = uses_only(palavra, letrasIndicadas)
        if verificacao == True :
            totalComIndicadas += 1
            print(palavra)
    
    print(f'De {totalPalavras} palavras, {totalComIndicadas} usam apenas letras indicadas!')

def letrasIndicadas1vez() :
    letrasIndicadas = getTextMin('Insira letras para Analise : ', 1)
    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalComIndicadas = 0

    for linha in arquivo :
        palavra = linha.strip()
        totalPalavras += 1

        if uses_all(palavra, letrasIndicadas) :
            print(palavra)
            totalComIndicadas += 1

    print(f'De {totalPalavras} palavras, {totalComIndicadas} usam letras indicadas pelo menos uma vez!')

def ordemAlfabetica() :
    arquivo = open('br-sem-acentos.txt')
    totalPalavras = 0
    totalEmOrdem = 0

    for linha in arquivo :
        palavra = linha.strip()
        totalPalavras += 1

        if is_abecedarian(palavra) :
            print(palavra)
            totalEmOrdem += 1

    print(f'De {totalPalavras} palavras, {totalEmOrdem} tem suas letras organizadas em ordem alfabética!')

def main() :
    opcao = -1

    while opcao != 0 :
        clearScreen()
        menu()
        opcao = getIntInRange(' > ', 0, 7)

        if opcao == 1 :
            mostrarTudo()
        elif opcao == 2 :
            mostrarMinimoCaracteres()
        elif opcao == 3 :
            palavrasSemE()
        elif opcao == 4 :
            letrasProibidas()
        elif opcao == 5 :
            letrasIndicadas()
        elif opcao == 6 :
            letrasIndicadas1vez()
        elif opcao == 7 :
            ordemAlfabetica()
        
        enterToContinue()
    clearScreen()    
    print('FIM!')

main()
    

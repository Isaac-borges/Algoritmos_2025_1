import os

def menu() :
    print('''
Brincadeira de nomes
          
1 - Add Nome
2 - List Nomes
3 - List Nomes in Arquivos

''')
    
def listarNomes(nomes) :
    for nome in nomes :
        print(nome)
    
def listarNomesArquivos() :
    arquivo = open('nome.txt')
    for palavra in arquivo :
        nome = palavra.strip()
        print(nome)

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')
    

def main() :
    listaNomes = []
    opcao = -1

    while opcao != 0 :
        clearScreen()
        menu()
        opcao = int(input(' > '))
        clearScreen()
        if opcao == 1 :
            nome = input('Nome : ')
            listaNomes.append(nome)
        if opcao == 2 :
            listarNomes(listaNomes)
        if opcao == 3 :
            listarNomesArquivos()

        input('ENTER to continue ...')

main()
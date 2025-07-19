import os 
from entradas import getIntInRange
def addNome():
    novoNome = str(input('Escreva um nome : '))

def countNome(num) :
    if num != 1 :
        texto = 'nomes escritos'
    else : 
        texto = 'nome escrito'
    print(f'{num} {texto} ')

def countLetra() :
    pass

def maiorNome() :
    pass

def menorNome() :
    pass

def menu():
    print('''
---------------------------------------------------------------          
                        CONTAR NOMES
        1 - ADICIONAR NOME
        2 - CONTAR NOMES
        3 - CONTAR LETRAS
        4 - MAIOR NOME
        5 - MENOR NOME
        0 - SAIR
                  
---------------------------------------------------------------          
          ''')
    

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def enterToContinue():
    input('Pressione ENTER ... ')

def main():
    opcao = None
    numNomes = 0
    
    while opcao != 0 :
        menu()
        opcao = getIntInRange('Opção : ', 0, 5)
        clearScreen()
        
        if opcao == 1 :
            novoNome = addNome()
            numNomes += 1
            enterToContinue()
        elif opcao == 2 :
            countNome(numNomes)
            enterToContinue()
        elif opcao == 3 :
            countLetra() 
        elif opcao == 4 :
            maiorNome()
        elif opcao == 5 :
            menorNome()
        
        clearScreen()


            


    clearScreen()
    print('FIM!')


main()
    
import os 

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')

def ENTERtoContinue() :
    input('Pressione ENTER ')

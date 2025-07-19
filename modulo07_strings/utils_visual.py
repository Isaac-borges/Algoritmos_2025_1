import os 

def main() :
    ...

def enterToContinue() :
    input('ENTER para continuar ...')

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__' :
    main()
    
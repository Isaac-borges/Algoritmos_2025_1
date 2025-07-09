import os

def main() :
    pass

def clearScreen() :
    os.system('cls' if os.name == 'nt' else 'clear')

def enterToContinue() :
    input('Pressione ENTER ... ')
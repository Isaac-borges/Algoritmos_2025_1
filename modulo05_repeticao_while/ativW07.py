from utils_float import getFloat

def main() :
    numero = getFloat('Insira um número : ')
    print(' - Inicio da lista -- ')
    lista = None
    while numero != lista :
        lista = getFloat('Insira um número : ')
    print(' --- Fim da lista --- ')

main()


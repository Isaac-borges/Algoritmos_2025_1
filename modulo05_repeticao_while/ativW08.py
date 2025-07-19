from utils_float import getFloat

def main() :
    numero = getFloat('Insira um número : ')
    print(' - Inicio da lista -- ')
    
    lista = numero
    listaAnterior = numero - 1

    while numero != lista + listaAnterior :
        listaAnterior = lista
        lista = getFloat('Insira um número : ')
        
    print(' --- Fim da lista --- ')

main()

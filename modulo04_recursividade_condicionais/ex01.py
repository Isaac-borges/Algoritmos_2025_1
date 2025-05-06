# Exercício 1: Verificador de Ano Bissexto
from entradas import getInt

def verificarBissexto(ano) : 
    resultado = 'não é bissexto'

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        resultado = 'é bissexto'

    return resultado


def main(): 
    ano = getInt('Insira : ')

    resultado = verificarBissexto(ano)

    print(f'O ano {ano} {resultado}')


main()
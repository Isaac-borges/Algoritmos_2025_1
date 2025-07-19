# 23. Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e
# escreva os N termos da PG. Ler o valor de N.
from utils_int import getPositiveInt
from utils_float import getFloat


def progressaoGeometrica(razao, primeiro_termo, qtd) :
    contador = 0
    print(primeiro_termo)
    termos = primeiro_termo
    while contador < qtd : 
        termos *= razao
        print(termos)
        contador += 1

def main() :
    razao = getFloat('Razão : ')
    primeiro_termo = getFloat('Primeiro termo : ')
    qtd_termos = getPositiveInt('Qtd de termos : ')

    progressaoGeometrica(razao, primeiro_termo, qtd_termos)
    
main()
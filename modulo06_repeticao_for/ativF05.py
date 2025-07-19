#5. Leia um número, calcule e escreva seu fatorial.
from utils_int import getPositiveInt

def main() :
    numero = getPositiveInt('Insira um número : ')
    fatorial = numero
    for i in range(numero-1, 0, -1):
        fatorial *= i
    
    print(f'O fatorial de {numero} é {fatorial}')

main()
#7. Leia um número N, some todos os números inteiros entre 1 e N e 
#escreva o resultado obtido.

from utils_int import getPositiveInt

def main() :
    numero = getPositiveInt('Insira um número : ')
    soma = 0
    for i in range(1, numero+1, 1) :
        soma += i
    
    print(f'A soma dos números de 1 a {numero} é : {soma}')

main()


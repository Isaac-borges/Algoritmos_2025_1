# 11. Leia quatro números (opção, num 1, num2, num3) e que escreva 
# o valor de num1 se opção igual a 1; o valor de num2 se opção for 
# igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores 
# possíveis para a variável opção são 1, 2 e 3.

from entradas import getIntInRange, getFloat

def main() :
    opcao = getIntInRange('Insira uma opção (1, 2, 3) : ', 1, 3)

    num1 = getFloat('Insira um número (1/3) : ')
    num2 = getFloat('Insira um número (2/3) : ')
    num3 = getFloat('Insira um número (3/3) : ')

    if opcao == 1 :
        print(num1)
    elif opcao == 2 :
        print(num2)
    else:
        print(num3)


main()
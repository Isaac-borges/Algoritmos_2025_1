from utils_float import getFloat

def main() :
    num = getFloat('Insira um número : ')

    if num > 0 :
        print('O número é positivo!')
    elif num < 0 :
        print('O número é negativo!')
    else :
        print('O número é zero!')

main()
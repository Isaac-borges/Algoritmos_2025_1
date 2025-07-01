# 15. Leia a quantidade de horas aula dadas por dois professores e o 
# valor por hora recebido por cada um. Escreva na tela qual dos professores 
# tem salário total maior.
from utils_float import getPositiveFloat
from utils_int import getPositiveInt

def main() :
    horaAula1 = getPositiveInt('Quantidades de horas ministradas pelo professor 1 : ')
    valor1 = getPositiveFloat('Valor que ele recebe por hora : ')
    horaAula2 = getPositiveInt('Quantidades de horas ministradas pelo professor 1 : ')
    valor2 = getPositiveFloat('Valor que ele recebe por hora : ')

    salario1 = horaAula1 * valor1
    salario2 = horaAula2 * valor2

    print(f'O professor 1 recebe R$ {salario1:.2f} e o professor 2, R$ {salario2:.2f}.')

main()
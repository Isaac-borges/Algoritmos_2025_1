# 13. Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
# descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
# somas. (Flag: salário=0)

# De Até                    Acréscimo
# R$ 0,00 R$ 2.999,99       25 %
# R$ 3.000,00 R$ 5.999,99   20 %
# R$ 6.000,00 R$ 9.999,99   15 %
# Acima de R$ 10.000,00     10 %

from utils_float import getFloatMin

def reajustar(salario) :
    reajuste = salario
    if salario < 3000 :
        reajuste *= 1.25
    elif salario < 6000 :
        reajuste *= 1.20
    elif salario < 10000 :
        reajuste *= 1.15
    else :
        reajuste *= 1.10

    return reajuste

def main() :
    total_normal = 0
    total_reajuste = 0

    salario = getFloatMin('Salario = R$ ', 0)
    while salario != 0 :
        total_normal += salario

        reajuste = reajustar(salario)
        total_reajuste += reajuste
        print(f'Salario  : R$ {salario:.2f}')
        print(f'Reajuste : R$ {reajuste:.2f}')

        salario = getFloatMin('Salario = R$ ', 0)

    print(f'''Soma dos salarios  : R${total_normal:.2f};
Soma dos reajustes : R$ {total_reajuste:.2f}
Diferença : R$ {(total_reajuste - total_normal ):.2f}''')
    
main()
    


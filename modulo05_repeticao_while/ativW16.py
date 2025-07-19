# 16. Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo.
# Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um
# algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.

from utils_float import getPositiveFloat

def simulacaoEmprestimo(valor) :
    contador = 0 #considerar primeiro dia como segunda
    valor_emprestimo = valor
    dias_uteis = 0
    while valor_emprestimo > 0 :
        valor_emprestimo += valor_emprestimo * 0.0085
        print(f'Valor atual : R${valor_emprestimo:.2f}')

        if contador % 7 >= 0 and contador % 7 <= 4 :
            valor_emprestimo -= 200 
            dias_uteis += 1
            print(f'Pagamento realizado, valor atual : R${valor_emprestimo:.2f}' if valor_emprestimo > 0 else 'Pagamento realizado, valor atual : R$ 0.00')
        else : 
            print('Nenhum pagamento realizado, não é dia útil.')

        contador += 1

    print(f'Pagamento concluído em {dias_uteis} dias uteis!')

def main() :
    emprestimo = getPositiveFloat('Valor do empréstimo : ')

    simulacaoEmprestimo(emprestimo)

main()
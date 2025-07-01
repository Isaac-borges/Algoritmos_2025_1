from entradas import getInt

def verificarBissexto(ano) :

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True



def validarData(d, m, a) :
    validade = ''
    if (m == 1 or m == 3 or m == 5 or m == 7 or
        m == 8 or m == 10 or m == 12) and d <= 31:
        validade = 'válida'
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d <= 30 :
        validade = 'válida'
    elif m == 2 and d <= 28 :
        validade = 'válida'
    elif verificarBissexto(a) and m == 2 and d <= 29 :
        validade = 'válida'
    else :
        validade = 'inválida'

    return validade


def main() :
    dia = getInt('Insira o dia : ')
    mes = getInt('Insira o mês : ')
    ano = getInt('Insira o ano : ')

    valido = validarData(dia, mes, ano)

    print(f'A data é {valido}')


if __name__ == '__main__' :
    main()
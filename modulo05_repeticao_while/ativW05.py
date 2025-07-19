from utils_int import getIntMin, getInt

def XporN(X, N) :
    Xabstrato = X
    Nabstrato = N

    while Nabstrato > 2 :
        divisao = Xabstrato / Nabstrato
        print(f'{Xabstrato} / {Nabstrato} = {divisao}')
        Nabstrato -= 1
        Xabstrato = divisao


def main() :
    X = getInt('Insira o valor de X : ')
    N = getIntMin('Insira o valor de N : ', 2)

    XporN(X, N)

main()


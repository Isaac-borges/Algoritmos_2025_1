# 18. Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
# crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
# crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
# necessários, para que a população da cidade A ultrapasse a população da cidade B.

def crescimento(valor, percentual) :
    return valor + (valor * percentual)

def main() :
    contador = 0
    populacao_cidade_A = 200_000
    populacao_cidade_B = 800_000
    while populacao_cidade_A <= populacao_cidade_B :
        populacao_cidade_A = crescimento(populacao_cidade_A, 0.035)
        populacao_cidade_B = crescimento(populacao_cidade_B, 0.0135)
        contador += 1

        print(f'Ano {contador} > Cidade A : {populacao_cidade_A:.0f}; Cidade B : {populacao_cidade_B:.0f}' )
    
    print(f'{contador} anos!')

main()
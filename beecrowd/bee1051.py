def calcularImposto(renda) :
    ate2000 = 2000
    ate3000 = 0
    imposto3000 = 0.08
    ate4500 = 0
    imposto4500 = 0.18
    maisde4500 = 0
    impostoMais4500 = 0.28

    if renda <= 2000 :
        return 'Isento'
    elif renda <= 3000 :
        ate3000 = (renda - ate2000) * imposto3000
    elif renda <= 4500 :
        ate4500 = renda - 3000
        ate3000 = renda - ate4500 - 2000
        ate4500 *= imposto4500
        ate3000 *= imposto3000
    elif renda > 4500 :
        maisde4500 = renda - 4500 
        ate4500 = renda - maisde4500 - 3000
        ate3000 = renda - maisde4500 - ate4500 - ate2000
        maisde4500 *= impostoMais4500
        ate4500 *= imposto4500
        ate3000 *= imposto3000
    
    totalImposto = ate4500+ ate3000 + maisde4500
    
    return f'R$ {totalImposto:.2f}'

def main() :
    renda = float(input(''))

    imposto = calcularImposto(renda)

    print(imposto)

main()
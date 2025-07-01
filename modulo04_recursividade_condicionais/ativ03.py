# 3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
from entradas import getFloat

#Essa função foi feita para ser usada tanto aqui, tanto na questão 5
def maiorORmeioORmenor(n1, n2, n3, solicitado) :
    #maior N1
    if n1 > n2 and n1 > n3 :
        maior = n1
        if n2 > n3 :
            meio = n2
            menor = n3
        else :
            meio = n3 
            menor = n2

    #MAIOR N2
    elif n2 > n1 and n2 > n3 :
        maior = n2
        if n1 > n3 :
            meio = n1 
            menor = n3
        else :
            meio = n3 
            menor = n1

    #MAIOR N3
    elif n3 > n1 and n3 > n2 :
        maior = n3 
        if n1 > n2 :
            meio = n1
            menor = n2
        else : 
            meio = n2
            menor = n1

    #IGUALDADES 
    if n1 == n2 :
        if n1 > n3 :
            maior = n1
            meio = n1
            menor = n3
        else :
            maior = n3
            meio = n1
            menor = n1
    elif n1 == n3 :
        if n1 > n2 :
            maior = n1
            meio = n1
            menor = n2
        else : 
            maior = n2
            meio = n1
            menor = n1       
    
    if solicitado == 'maior' :
        return maior
    elif solicitado == 'meio' :
        return meio
    elif solicitado == 'menor' :
        return menor
    

def main():
    numero1 = getFloat('Insira um número (1/3) : ')
    numero2 = getFloat('Insira um número (2/3) : ')
    numero3 = getFloat('Insira um número (3/3) : ')

    maiorNum = maiorORmeioORmenor(numero1, numero2, numero3, 'maior')

    print(f'O maior número é {maiorNum}.')

if __name__ == '__main__' :
    main()

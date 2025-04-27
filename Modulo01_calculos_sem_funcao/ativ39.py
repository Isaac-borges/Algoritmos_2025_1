# 39. Leia três números inteiros e positivos (A, B, C) e 
# calcule a seguinte expressão: 

#Entrada
numA = int(input('Número A : '))
numB = int(input('Número B : '))
numC = int(input('Número C : '))

#Processamento
numR = (numA + numB)**2
numS = (numB + numC)**2

numD = (numR + numS) / 2

#Saida

print(f'''
A resposta da equação       R + S
                      D =  -------
                              2
Onde, 
      R = (A+B)² ; R = ({numA}+{numB})² ; R = {numR}
    e,
      S = (B+C)² ; S = ({numB}+{numC})² ; S = {numS}

É, 
      D = {numR} + {numS} / 2 ; D = {numD * 2} / 2 ;
      D = {numD}


''')
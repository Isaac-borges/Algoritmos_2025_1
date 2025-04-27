# 43. Enunciado com mta imagem, fica sem sentido

#Entrada
numA = float(input('Insira A : '))
numB = float(input('Insira B : '))
numC = float(input('Insira C : '))
numD = float(input('Insira D : '))
numE = float(input('Insira E : '))
numF = float(input('Insira F : '))

#Processamento
numX = (numC*numE - numB*numF) / (numA*numE - numB*numD)
numY = (numA*numF - numC*numD) / (numA*numE - numB*numD)

#Saida
print(f'''
No sistema ax + by = c
           dx + ey = f
O valor de x é {numX} e o valor de y é {numY}
''')
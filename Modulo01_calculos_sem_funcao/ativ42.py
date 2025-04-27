# 42. Escreva um algoritmo que, tendo como dados de entrada 2 pontos 
# quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), 
# escreva a distância entre eles, conforme fórmula abaixo.

#Entrada
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

#Processamento
distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5

#Saida
print(f'A distância entre os pontos é {distancia}')
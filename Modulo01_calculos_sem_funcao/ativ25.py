# 25. Leia um número inteiro de metros, calcule e 
# escreva quantos Km e quantos metros ele corresponde.

#Entrada
distM = int(input('Insira uma distancia inteira em metros : '))

#Processamento
equivalenteKM = distM // 1000
equivalenteM = distM % 1000

#Saida
print(f'Essa distancia corresponde à {equivalenteKM} km e {equivalenteM} m')

# 6. Leia uma velocidade em km/h, calcule e 
# escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

#Entrada
velKMH = float(input('Insira uma velocidade em km/h : '))

#Processamento
velMS = velKMH / 3.6

#Saida
print(f'{velKMH} km/h equivale à {velMS} m/s! ')
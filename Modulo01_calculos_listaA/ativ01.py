#Escreva um programa que calcule a média 
#ponderada de três notas, considerando seus respectivos pesos.

#Entrada
nota1 = float(input('Digite a primeira nota: '))
peso1 = float(input('Digite o primeiro peso: '))
nota2 = float(input('Digite a segunda nota: '))
peso2 = float(input('Digite o segundo peso: '))
nota3 = float(input('Digite a terceira nota: '))
peso3 = float(input('Digite o terceiro peso: '))

#Processamento
media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

#Saida
print(f'A média é {media}')
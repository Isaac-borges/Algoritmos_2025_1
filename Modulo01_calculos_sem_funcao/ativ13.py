# 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

#Entrada
valorReal = float(input('Valor em real : R$ '))

#Processamento
desconto = valorReal * 0.7

#Saida
print(f'R$ {desconto:.2f}')
# Escreva um programa que calcule o montante final em uma
# aplicação financeira com juros simples.

#Entrada
capital = float(input('Capital Inicial    : R$ '))
taxa = float(input('Taxa (decimal)     : '))
tempo = float(input('Tempo de aplicação : '))

#Processamento
montante = capital + capital * taxa * tempo
#Saida
print(f'O montante final é : R$ {montante}')
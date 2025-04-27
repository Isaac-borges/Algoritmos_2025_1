# Escreva um programa que calcule o Índice de Massa Corporal (IMC), 
# dado o peso e a altura.

#Entrada
peso =   float(input('Insira o seu peso (kg) : '))  
altura = float(input('Insira sua altura (m)  : '))

#Processamento
imc = peso / (altura**2)

#Saida
print(f'Seu IMC é              : {imc:.2f}')
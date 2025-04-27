#Escreva um programa que calcule a soma 
#dos primeiros N números naturais.

#Entrada
numero = int(input('Numero: '))

#Processamento
somaNaturais = (numero * (numero+1)) / 2

#Saida
print(f'A soma dos naturais até {numero} é {somaNaturais}')
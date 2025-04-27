# 3. Leia um valor em minutos, calcule e escreva 
# o equivalente em horas e minutos.

#Entrada
valorMinutos = int(input('Minutos : '))

#Processamento
equivHoras = valorMinutos // 60
equivMinutos = valorMinutos % 60

#Saida
print(f'A quantidade {valorMinutos} de minutos equivale à {equivHoras} hora(s) e {equivMinutos} minuto(s)')
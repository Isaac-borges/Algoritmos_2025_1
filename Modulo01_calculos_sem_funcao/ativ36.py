#Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a
#expressa apenas em dias

#entrada 
anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

#processamento
total_dias = dias + (meses*30) + (anos*365)

#saida
print('Sua idade em dias é: ', total_dias, ' dias')
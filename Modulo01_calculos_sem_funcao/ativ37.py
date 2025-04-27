# 37. Leia a idade de uma pessoa expressa em dias e 
# escreva-a expressa em anos, meses e dias.

#Entrada
idadeDias = int(input('Escreva a idade de uma pessoa em dias : '))

#Processamento
expressoAnos = idadeDias // 365
restoAnos = idadeDias % 365
print(restoAnos)
expressoMeses = restoAnos // 30
expressoDias = restoAnos % 30

#Saida
print(f'A idade dele em anos pode ser expressa em {expressoAnos} anos, {expressoMeses} meses e {expressoDias} dias')


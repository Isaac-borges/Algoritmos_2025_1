#Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#Entrada
numMeses = int(input('Diga um número inteiro de meses: '))

#Processamento
numAnos = numMeses//12
restoMeses = numMeses%12

#Saida
print(f'{numAnos} ano(s) e {restoMeses} mes(es)')
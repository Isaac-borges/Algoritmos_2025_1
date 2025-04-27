# Escreva um programa que calcule quanto tempo 
# levará uma viagem, dado a distância e a velocidade média.

# Entrada
distancia = float(input('Distancia (km): '))
velocidadeMedia = float(input('Velocidade média (km/h): '))

# Processamento
tempoViagem = distancia / velocidadeMedia

# Saida
print(f'O tempo de viagem será: {tempoViagem} horas')
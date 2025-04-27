# 40. Calcule a quantidade de dinheiro gasta por um fumante. 
# Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados 
# por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

#Entrada
anosDeFumo = int(input('Há quantos anos você fuma? : '))
numeroCigarros = int(input('Quantos cigarros você fuma por dia? : '))
precoCarteira = float(input('Qual o preço de uma carteira de cigarro? : '))

#Processamento
carteirasDia = (numeroCigarros // 20) + 1
precoTotal = (carteirasDia * precoCarteira) * (anosDeFumo * 365)

#Saida
print(f'Esse fumante gastou R$ {precoTotal:.2f}')
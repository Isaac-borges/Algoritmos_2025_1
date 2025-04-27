# 44. Sabendo que latão é constituído de 70% de cobre e 30% 
# de zinco, escreva um algoritmo que calcule a quantidade de 
# cada um desses componentes para se obter certa quantidade 
# de latão (em kg), informada pelo usuário.

#Entrada
pesoLatao = float(input('Quantidade de latão em kg : '))

#Processamento
pesoCobre = 0.7 * pesoLatao
pesoZinco = 0.3 * pesoLatao

#Saida 
print(f'Essa quantidade de latão é constituída por {pesoCobre} kg de cobre e {pesoZinco} kg de zinco!')
# 10. Leia 2 números inteiros, calcule e escreva 
# o quociente e o resto da divisão do 1o pelo 2o.

#Entrada
num1 = int(input('1º número : '))
num2 = int(input('2º número : '))

#Processamento
quociente = num1 // num2 
resto = num1 % num2

#Saida
print(f'''
      {num1}/{num2}
O quociente da divisão é : {quociente}
O resto da divisão é     : {resto}
''')
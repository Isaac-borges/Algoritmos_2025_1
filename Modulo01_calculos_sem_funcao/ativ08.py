# 8. Leia 2 números, calcule e escreva a 
# divisão da soma pela subtração dos números lidos.

#Entrada
num1 = float(input('1º Numero : '))
num2 = float(input('2º Numero : '))

#Processamento
soma = num1 + num2
subtracao = num1-num2
divisao = soma / subtracao

#Saida
print(f'''
A soma dos números {num1} e {num2} é :
                        >>>> {soma}
A diferença destes mesmos números é : 
                        >>>> {subtracao}
E a divisão entre eles ({soma}/{subtracao}) é :
                        >>>> {divisao}

''')

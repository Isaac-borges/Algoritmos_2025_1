#3. Leia as variáveis A0, Limite e R e escreva os valores menores que 
# Limite gerados pela Progressão Aritmética que tem por valor inicial 
# A0 e razão R.
from utils_int import getIntMin, getInt
def main() :
    A0 = getInt('Insira o primeiro termo : ')
    Limite = getIntMin('Insira o limite : ', A0)
    Razao = getIntMin('Insira a razão : ', 1)
    

    for i in range(A0, Limite, Razao) :
        print(i)

main()
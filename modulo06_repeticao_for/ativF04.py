from utils_int import getIntMin, getInt
def main() :
    A0 = getInt('Insira o primeiro termo : ')
    Limite = getIntMin('Insira o limite : ', A0)
    Razao = getIntMin('Insira a razão : ', 1)
    prog = A0

    for i in range(A0, Limite, 1) :
        i -= 1
        prog *= Razao
        i = prog
        print(i)
        
    

main()
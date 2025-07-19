def main() :
    senhaCorreta = 2002
    senha = None

    while senha != senhaCorreta :
        senha = int(input(''))

        if senha != senhaCorreta :
            print('Senha Invalida')
    
    print('Acesso Permitido')

main()
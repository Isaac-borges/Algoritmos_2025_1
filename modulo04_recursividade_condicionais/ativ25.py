# 25. Verifique a validade de uma senha fornecida pelo usuário. A senha
# é 1234. O algoritmo deve escrever uma mensagem de permissão de acesso
# ou não.
def verificarSenha(senhaInserida, senhaReal) :
    if senhaInserida != senhaReal :
        return False
    else: 
        return True

def main() :
    tentativaSenha = input('Insira a senha : ')
    senhaReal = '1234'

    if verificarSenha(tentativaSenha, senhaReal) :
        print('Bem vindo!')
    else:
        print('Acesso negado!')

main()
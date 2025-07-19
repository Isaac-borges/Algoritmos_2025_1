def main() :
    while True :
        m, n = input('').split()
        m, n = int(m), int(n)

        if m <= 0 or n <= 0 :
            break

        maior = m if m >= n else n
        menor = m if m <= n else n
        texto = ''
        soma = 0

        for i in range(menor, maior + 1, 1) :
            texto += f'{i} '
            soma += i

        texto += f'Sum={soma}'
        print(texto)

main()
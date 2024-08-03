numero = int(input('Digite um número: '))
total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[33m', end='')
    print(c, end=' ')

print(f'\n\033[mO número {numero} foi divisível {total} vezes.')

if total == 2:
    print(f'Por isso o número {numero} é considerado como primo')
else:
    print(f'Por isso o número {numero} não é considerado primo!')
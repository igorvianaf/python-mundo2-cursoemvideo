#solução usando biblioteca
# from math import factorial

# n = int(input('Digite um número para calcular o seu fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

n = int(input('Digite um valor para saber seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 
print(f'{f}')
    
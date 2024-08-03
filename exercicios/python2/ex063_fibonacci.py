print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você deseja mostrar: '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2} ', end='')

#começou do termo 3 porque já tinha sido declarado os termos 1 e 2
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'→ {t3} ', end='')
#transformando t1 em t2 e t2 em t3 para somar com o proximo numero
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')

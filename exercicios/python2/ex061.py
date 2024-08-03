primeiro = int(input('Digite o primeiro termo: '))
r = int(input('Informe a razão: '))
termo = primeiro
c = 1

while c <= 10:
    print(f'{termo} → ', end='')
    termo += r
    c += 1

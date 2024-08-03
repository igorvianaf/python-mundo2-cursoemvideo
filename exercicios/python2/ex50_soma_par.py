soma_par = 0
cont = 0

for c in range (0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma_par += numero
        cont += 1

print(f'Foram digitados {cont} números pares. O resultado da soma é: {soma_par}')
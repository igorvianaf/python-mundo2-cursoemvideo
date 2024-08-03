numero = soma = contador = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    
    if numero == 999:
        break

    soma += numero
    contador += 1

print(f'Foram digitados {contador} valores, a soma entre eles é de {soma}')

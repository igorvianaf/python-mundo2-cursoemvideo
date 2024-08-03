maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    
    peso = float(input('Digite o seu peso em KG: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso >= maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso
    
print(f'O maior peso é {maior_peso} e o menor peso é {menor_peso}')
    
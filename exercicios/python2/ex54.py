from datetime import date

data_atual = date.today().year
maior_idade = 0
menor_idade = 0
for c in range(1, 8):
    data = int(input(f'Em que ano a {c}ª pessoa nasceu: '))

    if data_atual - data >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
        
print(f'{maior_idade} pessoas são considerados maior de idade e {menor_idade} são considerados menor de idade')
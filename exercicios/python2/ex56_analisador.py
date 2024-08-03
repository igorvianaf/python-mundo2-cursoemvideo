cont_idade = 0
maior_idade_homem = 0
nome_velho = ''
mulher_20 = 0


for p in range(1, 5):
    print('-' * 5, f'{p}ª PESSOA', '-' *5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    cont_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade >= maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher_20 += 1

media_idade = cont_idade / 4

print(f'A média de idade do grupo é de {media_idade}.')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_velho}.')
print(f'Ao todo são {mulher_20} mulheres com menos de 20 anos.')
    



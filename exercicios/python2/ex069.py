cont_idade = cont_homem = cont_mulherers = 0



while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
    
    if idade >= 18:
        cont_idade += 1
    
    if sexo in 'M':
        cont_homem += 1
    
    if sexo in 'F' and idade <= 20:
        cont_mulherers += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    
    if continuar == 'N':
        break

    

print(f'Quantidade de pessoas maior de 18 anos: {cont_idade}')
print(f'Quantidade de pessoas do sexo masculino: {cont_homem}')
print(f'Quantidade de mulheres com menos de 20 anos: {cont_mulherers}')

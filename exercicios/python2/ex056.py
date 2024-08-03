soma_idade = 0

for c in range(1, 4):
    nome = input('Digite seu nome: ')
    idade = float(input('Digite sua idade: '))
    sexo = input('Qual o seu sexo? [M/F]')

    if idade == True:
        soma_idade += idade

print(soma_idade / 4)


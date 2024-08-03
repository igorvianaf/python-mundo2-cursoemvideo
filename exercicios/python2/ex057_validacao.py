sexo = input('Informe seu sexo [M/F]: ').upper().strip()[0]

while sexo not in 'FfMm':
    sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F] : ').strip().upper()

print(f'Sexo {sexo} registrado com sucesso!')

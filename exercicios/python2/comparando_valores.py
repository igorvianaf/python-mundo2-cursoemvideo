numero_um = input('Digite um número inteiro: ')
numero_dois = input('Digite outro número inteiro: ')

numero_um_int = int(numero_um)
numero_dois_int = int(numero_dois)

if numero_um_int > numero_dois_int:
    print(f'{numero_um_int} é maior que {numero_dois_int}')
elif numero_dois_int > numero_um_int:
    print(f'{numero_dois_int} é maior que {numero_um_int}')
else:
    print('Os valores são iguais')
    
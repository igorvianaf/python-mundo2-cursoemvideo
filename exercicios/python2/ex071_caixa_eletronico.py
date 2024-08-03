valor = int(input('Informe o valor que você deseja sacar: R$ '))
total = valor

cedula = 50
total_cedula = 0

while True:
    #condição para diminuir o valor de cada cedula pelo valor total informado
    if total >= cedula:
        total -= cedula
        #contador para quantidade de cédulas
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de {cedula}')
        #checando cedulas e alterando valor       
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
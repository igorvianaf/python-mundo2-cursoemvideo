from datetime import date

data_atual = date.today().year
nasc_int = input('informe o ano que você nasceu: ')
nasc_int = int(nasc_int)
idade_atleta = data_atual - nasc_int

print(f'O atleta tem {idade_atleta} anos')

if idade_atleta <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade_atleta <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade_atleta <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade_atleta <= 25:
    print('CLASSIFICAÇÃO: SENIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')

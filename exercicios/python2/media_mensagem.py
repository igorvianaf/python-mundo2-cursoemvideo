nota_1 = input('Informe a primeira nota: ')
nota_2 = input('Informe a segunda nota: ')

nota_1_float = float(nota_1)
nota_2_float = float(nota_2)
media = (nota_1_float + nota_2_float) / 2

if media < 5:
    print(f'Sua média foi {media:.1f}. Você foi reprovado')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media:.1f}. Você está em recuperação')
elif media > 7 and media <= 10:
    print(f'Parábens, sua média é {media:.1f}. Você foi aprovado!')
else:
    print('Digite um número válido entre 0 e 10')
    
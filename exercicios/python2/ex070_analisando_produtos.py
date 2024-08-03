import os

compra_total = 0
produtos_mil = 0
valor_mais_barato = 0
nome_mais_barato = ' '

print('=' * 30)
print('Loja Teste')
print('=' * 30)


while True:
    produto = input('Informe o nome do produto: ')
    preco = float(input('Quanto custo o produto informado: R$ '))

    compra_total += preco

    if preco >= 1000:
        produtos_mil += 1
    
    if valor_mais_barato == 0 or preco < valor_mais_barato:
        valor_mais_barato = preco
        nome_mais_barato = produto

    verificacao = ' '        
    while verificacao not in 'SN':
        print('=' * 30)
        verificacao = input('Você deseja continuar? [S/N] ').strip().upper()[0]
        print('=' * 30)
    
    if verificacao == 'N':
        break




print(f'O total gasto na compra foi de {compra_total}')
print(f'{produtos_mil} produtos custaram mais que R$1000')
print(f'{nome_mais_barato} é o produto mais barato e custa R$ {valor_mais_barato}')
        

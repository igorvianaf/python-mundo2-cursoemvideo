#solicitando entrada para informação do produto
valor_do_produto = input('Qual o valor do produto: ')
print('''Formas de Pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartao
[3] 2x no cartão
[4] 3x ou mais no cartão''')

condicao_pagamento = input('Informe a forma de pagamento: ')

#alterando a variavel str para float
valor_do_produto_float = float(valor_do_produto)

#informando os descontos dos produtos
avista_dinheiro = valor_do_produto_float - (10/100 * valor_do_produto_float)
avista_cartao = valor_do_produto_float - (5/100 * valor_do_produto_float)
tres_vezes_cartao = valor_do_produto_float + (20/100 * valor_do_produto_float)

#condições para o pagamento
if condicao_pagamento == '1':
    print(f'O produto custava {valor_do_produto} e você irá pagar apenas R$: {avista_dinheiro:.2f}, com 10% de desconto')
elif condicao_pagamento == '2':
    print(f'O produto custava {valor_do_produto} e você irá pagar apenas R$: {avista_cartao:.2f}')
elif condicao_pagamento == '3':
    print(f'O produto irá custar R$: {valor_do_produto_float:.2f} dividido em 2x sem juros')
elif condicao_pagamento == '4':
#input para saber a quantidade de parcelas
    parcelas = int(input('Quantidade de parcelas: '))
#se as parcelas forem maior ou igual a três está dentro da forma de pagamento    
    if parcelas >= 3:
        print(f'Sua compra será parcelada em {parcelas} com juros')
        print(f'Dividindo em {parcelas} temos juros de 20%. O produto irá custar: R$ {tres_vezes_cartao:.2f}')
#se parcelas menor que três não teram juros, então retornará quantidade invalida
    else: 
        print('Número de parcelas inválido')
else:
    print('Informe uma condição de pagamento válida')
#input para coletar os valores desejados
valor_do_imovel = input('Qual o valor da casa que você deseja comprar? R$: ')
salario = input('Informe seu salário R$: ')
tempo_pagamento = input('Em quantos anos você deseja pagar: ')

#transformando str em num para calculos
valor_do_imovel_float = float(valor_do_imovel)
salario_float = float(salario)
tempo_pagamento_int = int (tempo_pagamento)
#criando variaveis para calculo
porcentagem_salario = 30/100 * salario_float
prestacao = valor_do_imovel_float / (tempo_pagamento_int * 12)

#condicao para emprestimo
if prestacao <= porcentagem_salario:
    print('Parábens, seu emprestimo foi aprovado')
    print(f'O valor mensal do imóvel é de R$: {prestacao:.2f} mensal')
else:
    print('Emprestimo negado')
    
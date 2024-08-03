import os

condicao = True
soma = qtd_valores = 0
maior_valor = 1
menor_valor = 1 


while condicao:
    numeros = int(input('Digite um número: '))
    qtd_valores += 1
    soma += numeros

    if menor_valor == 1:
        menor_valor = maior_valor = numeros
    else:    
        if numeros < menor_valor:
            menor_valor = numeros
        
        if numeros > maior_valor:
            maior_valor = numeros

    opcao = input('Deseja continuar adicionando valores? [S/N]: ').strip().upper()[0]
    if opcao in 'Ss':
        continue
    elif opcao in 'Nn':
        condicao = False
    else:
        print('Opção inválida')


os.system('cls')
print(f'Você digitou {qtd_valores} números e a media entre todos os valores digitados é: {soma / qtd_valores}')
print(f'O menor valor digitado foi: {menor_valor}')
print(f'O maior valor digitado foi: {maior_valor}')

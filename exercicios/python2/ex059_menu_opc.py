from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
#opcao começando com valor 0
opcao = 0

#atribuindo condicao para que o loop só acabe quando for escolhido o 5
while opcao != 5:
#menu de opção
    print(
'''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa'''
)
#entrada para mudar a variavel opcao
    opcao = int(input('Escolha sua opção: '))
    print('=-' * 10)
#condicão para opcao soma
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma} ')
#condicão para opcao multiplicação        
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação de {n1} e {n2} é {multiplicacao}')
#condicão para opcao maior ou igual         
    elif opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}')

        elif n1 < n2:
            print(f'O número {n1} é menor que {n2}')
            
        else:
            print(f'{n1} é igual a {n2}')
#atribuindo novos numeros a n1 e n2         
    elif opcao == 4:
        n1 = int(input('Novo valor: '))
        n2 = int(input('Novo valor: '))
#opção sair
    elif opcao == 5:
        print('Finalizando...')
#condição para números diferentes do menu        
    else:
        print('Opção inválida')
    print('-=' * 20)
    sleep(2)
print('Fim do programa')

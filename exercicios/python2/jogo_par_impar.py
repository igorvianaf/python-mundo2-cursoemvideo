import random
import os

print('=-' * 20)
print('Bem vindo ao jogo de par ou ímpar!!')
print('=-' * 20)
vitoria = 0

while True:
    
    jogador = int(input('Digite um valor: '))
    escolha_par_impar = input('Par ou Ímpar? [P/I]: ').upper().strip()[0]

    escolha_computador = random.randint(0, 9)
    
    soma = escolha_computador + jogador
    par = soma % 2 == 0
    impar = soma % 2 == 1
    

    #verificando se o usuario ganhou
    if escolha_par_impar in 'Pp' and par:
        os.system('cls')
        print(f'Você jogou {jogador} e o computador jogou {escolha_computador}.', end=' ')
        print(f'O resultado foi {soma}. deu Par')
        print('Você venceu!')
        print('=-' * 20)
        print('Vamos jogar novamente...')
        vitoria += 1

    elif escolha_par_impar in 'Ii' and impar:
        os.system('cls')
        print(f'Você jogou {jogador} e o computador jogou {escolha_computador}.', end=' ')
        print(f'O resultado foi {soma}. deu Ímpar')
        print('Você venceu!')
        print('=-' * 20)
        print('Vamos jogar novamente...')
        vitoria += 1


    #condição para o computador ganhar e retornar mensagem se o número foi par ou ímpar
    else:
        if par:
            os.system('cls')
            print(f'O computador escolheu {escolha_computador} e você escolheu {jogador}', end=' ')
            print(f'A soma entre eles é de {soma}. Um número par')
            print('=-' * 20)
            print('VOCÊ PERDEU!!')
            print('=-' * 20)
            print('GAME OVER!!')
            print(f'Você venceu {vitoria} vezes')
            break

        else:
            os.system('cls')
            print(f'O computador escolheu {escolha_computador} e você escolheu {jogador}.', end=' ')
            print(f'A soma entre eles é de {soma}. Um número ímpar')
            print('=-' * 20)
            print('GAME OVER!!')
            print('=-' * 20)
            print(f'Você venceu {vitoria} vezes')
            break

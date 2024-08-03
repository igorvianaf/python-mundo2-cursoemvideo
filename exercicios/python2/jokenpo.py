#importando biblioteca para escolha aleatoria
from random import choice

#entrada de escolha do usuario
entrada = input('Escolha entre pedra, papel e tesoura: ')

#lista para resposta do pc
a = 'pedra'
b = 'papel'
c = 'tesoura'

lista = [a, b, c]
escolha_pc = choice(lista)

#condição para ganhar, perder ou empatar
if entrada == 'pedra' and escolha_pc == 'papel':
    print(f'O computador escolheu {escolha_pc}. Você perdeu!')
elif entrada == 'pedra' and escolha_pc == 'tesoura':
    print(f'O computador escolheu {escolha_pc}. Parabéns, você ganhou!')
elif entrada == 'pedra' and escolha_pc == 'pedra':
    print(f'O computador escolheu {escolha_pc}. Empatou')
elif entrada == 'tesoura' and escolha_pc == 'papel':
    print(f'O computador escolheu {escolha_pc}. Parabéns, você ganhou!')
elif entrada == 'tesoura' and escolha_pc == 'tesoura':
    print(f'O computador escolheu {escolha_pc}. Empatou')
elif entrada == 'papel' and escolha_pc == 'papel':
    print(f'O computador escolheu {escolha_pc}. Empatou')
else:
    print('Entrada inválida')
    
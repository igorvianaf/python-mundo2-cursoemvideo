from random import randint
from time import sleep

n = randint(1,10)
print('O computador está escolhendo um número')
print('PROCESSANDO...')
sleep(3)
print('Número escolhido!')
print(('Escolhi um número entre 0 e 10. Você consegue adivinhar qual foi? '))
palpites = 0
escolha_usuario = int(input('Qual o seu palpite? '))

while escolha_usuario != n:
    if escolha_usuario > n:
        print('Menos... tente novamente')
        escolha_usuario = int(input('Qual é o seu palpite: '))
        palpites += 1
        
    elif escolha_usuario < n:
        print('Mais... tente novamente')
        escolha_usuario = int(input('Qual é o seu palpite: '))
        palpites += 1

print(f'Pensei no {n}. Você acertou com {palpites} tentativas. Parábens')

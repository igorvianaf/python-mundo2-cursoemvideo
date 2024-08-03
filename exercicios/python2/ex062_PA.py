print('GERADOR DE P.A.')
print('=-=' * 30)
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
total = 0
mais = 10

#enquanto a variavel mais for diferente de 0, loop
while mais != 0:
#a variável total começa com 10 valores atribuidos a ela    
    total = total + mais    
#utilizado o c para contar ate o valor total, informado pelo usuario no fim do loop
    while c <= total:
        print(f'{n1} → ', end='')
        n1 += r
        c += 1
    print('Pausa')
#alteramos a variavel mais dentro do loop para adicionar mais valores, caso o usuario queira 
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados')

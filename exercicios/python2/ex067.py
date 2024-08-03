import os

while True:
    
    numero = int(input('Quer ver a tabuada de qual valor? '))
    
    if numero > 0:
        os.system('cls')
        print(f'A tabuada de {numero} é: ')
        print(20 * '-')
        for c in range(1, 11):
            print(f'{c} x {numero} = {c * numero}')
    else:
        break 
print('PROGRAMA TABUADA ENCERRADO!!')
print('VOLTE SEMPRE!!')

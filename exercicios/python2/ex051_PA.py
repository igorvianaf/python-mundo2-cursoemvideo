print('GERADOR DE P.A.')
print('=-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print(f'{c} → ', end='')
    
print('FIM')
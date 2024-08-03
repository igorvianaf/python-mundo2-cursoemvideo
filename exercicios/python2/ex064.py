n1 = quantidade_digitada = soma = 0

while n1 != 999:
    
    n1 = int(input('Digite um número: [999 para parar] '))
    
    if n1 != 999:
        soma += n1
        quantidade_digitada += 1

    
    
print(f'Você digitou {quantidade_digitada} números e a soma entre eles foi {soma}')
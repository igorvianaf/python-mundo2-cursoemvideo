#input para coletar peso e altura
peso = input('Qual o seu peso? (Kg) ')
altura = input('Qual a sua altura? (m) ')

#alterando as variaveis para float
peso_float = float(peso)
altura_float = float(altura)

#cálculo de IMC
imc = peso_float / (altura_float ** 2)

#condições para descobrir o imc
if imc < 18.5:
    print(f'Seu imc é de {imc:.1f}. Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu imc é de {imc:.1f}. Você está na faixa de peso normal')
elif 25 <= imc < 30:
    print(f'Seu imc é de {imc:.1f}. Você está com sobrepeso')
elif 30<= imc < 40:
    print(f'Seu imc é de {imc:.1f}. Você está com obesidade')
elif imc >= 40:
    print(f'Seu imc é de {imc:.1f}. Você está com obesidade mórbida')
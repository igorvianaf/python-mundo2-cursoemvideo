#importar biblioteca datetime - ano
from datetime import date

#solicitando data de nascimento

ano_nascimento = input('Em que ano você nasceu? ')
data_atual = date.today().year
ano_nascimento_int = int(ano_nascimento)
idade = data_atual - ano_nascimento_int
tempo_para_alistamento = 18 - idade 
tempo_passado = idade - 18


#condições para alistamento
if idade < 18:
    print(f'Você tem {idade} anos e ainda precisa se alistar no serviço militar')
    print(f'Você tem {tempo_para_alistamento} para ir ao serviço militar')
elif idade == 18:
    print(f'Você tem {idade} e está na hora de se alistar para o serviço militar')
else:
    print(f'Você tem {idade} anos e fazem {tempo_passado} anos que você deveria ter se alistado')

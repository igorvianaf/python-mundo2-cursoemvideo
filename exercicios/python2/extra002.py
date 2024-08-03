produto = float(input('Informe o valor do produto: '))
avista = produto - (produto * 10 / 100)
aprazo = produto + (produto * 5 / 100)
print(f'O produto custa {produto}, se você pagar a vista irá custar {avista}, se dividir custará {aprazo}')

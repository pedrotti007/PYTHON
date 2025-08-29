quant_max = 1000
quant_min = 100

quant_real = float(input('Digite a quantidade atual em estoque:'))

quant_media = (quant_max + quant_min) / 2

if  quant_real < quant_media:
    print(f'Realize uma compra, o estoque é menor que {quant_min}!')
else:
    print(f'Não é nescessário uma compra, o estoque é maior que: {quant_min}')

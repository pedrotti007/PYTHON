nome=input("Olá, como posso te chamar:")

vdc= float(input(f"Certo, {nome}, por favor digite o valor da compra: R$"))

if vdc > 100: 
        desconto = 0.10

elif 50 <= vdc <= 100:
        desconto = 0.05

else:
        desconto = 0.00

valor_desconto = vdc * desconto
vtt = vdc - valor_desconto

print((f"{nome}, o valor descontado é: R${valor_desconto}"))
print((f"O valor total ficou em: R${vtt}"))
print((f'Tenha um otimo dia!'))
nome=input("Olá Boa Tarde, como se chama?")

nma= int(input(f"Certo {nome}, quantas maçãs deseja comprar?:"))

if nma < 12: 
    valor = 1.30

else:
    valor = 1.00

valor_total = nma * valor

print(f"{nome}, o valor total é: R${valor_total}!")
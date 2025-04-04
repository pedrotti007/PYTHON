vlr = float(input("Insira seu salário mensal:"))


if 0 < vlr <= 2000:
    print(f"Salário sem imposto! R$ {vlr}, tais pobre viss")
    
elif 2000.00 <= vlr <= 3500:
    imposto = vlr * 0.10
    print(f"Seu imposto sera de R$ {imposto}")
    print(f"Seu salário é no valor de R$ {vlr}")

elif vlr > 3.500:
    imposto = vlr * 0.10
    print(f"Seu imposto sera de R$ {imposto}")
    print(f"Seu salário é no valor de R$ {vlr}")
    
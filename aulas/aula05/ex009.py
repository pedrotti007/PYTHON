nota_1 = float(input("Digite a primeria nota:"))
nota_2 = float(input("Digite a segunda nota:"))

media = (nota_1 + nota_2) / 2

if media >= 6:
    print(f"Aprovado, com media: {media}")
else:
    print(f"Reprovado, com média: {media}")

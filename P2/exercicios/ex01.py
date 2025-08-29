
alturas = []
alturas_homens = []
contador_mulheres = 0


for i in range(1, 16):
    print(f"\nPessoa {i}:")
    

    while True:
        try:
            altura = float(input("Digite a altura (em metros): "))
            if altura <= 0:
                print("Altura deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    while True:
        genero = input("Digite o gênero (M para Masculino, F para Feminino): ").strip().upper()
        if genero in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Use 'M' ou 'F'.")


    alturas.append(altura)
    if genero == 'M':
        alturas_homens.append(altura)
    else:
        contador_mulheres += 1

maior_altura = max(alturas)
menor_altura = min(alturas)

if alturas_homens:
    media_altura_homens = sum(alturas_homens) / len(alturas_homens)
else:
    media_altura_homens = 0 


print("\n--- RESULTADOS ---")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_altura_homens:.2f} m")
print(f"Número de mulheres no grupo: {contador_mulheres}")

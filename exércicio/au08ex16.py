amigos = []

print("Digite os nomes dos seus amigos:")
print("Quando terminar, apenas pressione Enter sem digitar um nome.")


while True:

  nome_amigo = input("Amigo: ")


  if nome_amigo == "":
 
    break
  else:

    amigos.append(nome_amigo)


if amigos: 
  print("\n Seus Amigos ")

  for amigo in amigos:
    print(amigo)
else:

  print("\nVocê não adicionou nenhum amigo :().")
# a numeracao é feita a partir do "0"
lista_jogos = [
    'Call of Duty',
    'Fifa',
    'Rocket League',
    'Content Warning'
]
#lista toda
print(lista_jogos)

#puxar algo da lista utiliza o: []
print(lista_jogos[2])

while True:
    print(f'{lista_jogos[0]}, é so dor de cabeca')
    print(f'{lista_jogos[1]}, ate que vale a pena')
    print(f'{lista_jogos[2]}, da pra tentar se divertir')
    print(f'{lista_jogos[3]}, da medinho.')
    break
print('-------------')
print(            )
print(len('234245'))
print(            )

for i in range(len(lista_jogos)):
    print(f'{i + 1}. O jogo arretado é: {lista_jogos[i]}')




lado1 = float(input('Digite o valor do primeiro lado:'))
lado2 = float(input('Digite o valor do seguno lado:'))
lado3 = float(input('Digite o valor do terceiro lado:'))


if lado1 == lado2 == lado3:
    print('Triangulo Equilatero')

# usar o 'and' em vez de 'or'
elif lado1 != lado2 and lado3 != lado2 and lado1 != lado3:
    print('Triangulo Escaleno')
    
if not (lado1 == lado2 == lado3) and (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print('Triangulo Isóceles')


    
    
    
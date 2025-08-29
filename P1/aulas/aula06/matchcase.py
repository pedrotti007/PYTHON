
dia = int(input('Dia:'))

match dia:
    case 1:
        print('Dia Util')
    case 2:
        print('Final de semana de feriado')
    case _:
        print(F'Valor {dia} invalido')
    
    
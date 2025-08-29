def verificar_aprovacao():
    
    try:
        nota1 = float(input("Digite a nota da primeira avaliação: "))
        nota2 = float(input("Digite a nota da segunda avaliação: "))

        
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            raise ValueError("As notas devem estar entre 0 e 10.")

       
        media = (nota1 + nota2) / 2

        
        if media >= 6:
            situacao = "aprovado"
        else:
            situacao = "reprovado"

    
        print(f"A média do aluno é: {media:.2f}")
        print(f"O aluno está {situacao}.")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


verificar_aprovacao()
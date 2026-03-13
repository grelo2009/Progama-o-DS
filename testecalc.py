# Calculadora Simples em Python

def calculadora():
    print("Selecione a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    # Recebe a escolha do usuário
    escolha = input("Digite a opção (1/2/3/4): ")

    # Verifica se a opção é válida
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Digite números.")
            return

        if escolha == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif escolha == '4':
            # Trata a divisão por zero
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Erro: Divisão por zero não permitida.")
    else:
        print("Opção inválida.")

# Executa a calculadora
calculadora()

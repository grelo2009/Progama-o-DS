# 7. Calculadora de Desconto
# Solicite o preço de um produto e um código de desconto A ,B ou C.
# Aplique o desconto correspondente ao código e exiba o preço final.

# Definindo os descontos
descontos = {
    "A": 0.10,  # 10%
    "B": 0.20,  # 20%
    "C": 0.30   # 30%
}

# Entrada de dados
preco = float(input("Digite o preço do produto: "))
codigo = input("Digite o código de desconto (A, B ou C): ").upper()

# Verificação e cálculo
if codigo in descontos:
    desconto = descontos[codigo]
    preco_final = preco * (1 - desconto)
    print(f"Preço final com desconto {codigo}: R$ {preco_final:.2f}")
else:
    print("Código de desconto inválido. Nenhum desconto aplicado.")
    print(f"Preço final: R$ {preco:.2f}")

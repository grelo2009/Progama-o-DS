# 1. Definimos o nome da variável como 'letra' para que o 'if' funcione
letra = input("Digite uma letra: ").lower()

# Verifica se a letra está dentro da string de vogais
if letra in "aeiou":
    # 2. Se a condição for verdadeira, imprime "Vogal."
    print("Vogal.")
else:
    # 3. Caso contrário, imprime "Consoante."
    print("Consoante.")

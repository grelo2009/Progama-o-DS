import random

print("Bem-vindo ao jogo de adivinhação!")
print("Escolha o nível de dificuldade: Fácil, Médio ou Difícil.")

# Captura a escolha do usuário
nivel = input("Digite sua escolha: ").strip().lower()

# Define intervalo de acordo com a dificuldade
if nivel == "fácil":
    limite = 10
elif nivel == "médio":
    limite = 50
elif nivel == "difícil":
    limite = 100
else:
    print("Opção inválida! O jogo será configurado no nível Fácil por padrão.")
    limite = 10

# Gera número secreto conforme o nível
numero_secreto = random.randint(1, limite)
max_tentativas = 5

print(f"Tente adivinhar o número que estou pensando, entre 1 e {limite}. Você tem {max_tentativas} tentativas.")

# Loop do jogo
for tentativa in range(max_tentativas):
    palpite = int(input(f"Tentativa {tentativa + 1}/{max_tentativas}. Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    else:
        print("Quase lá! Tente um número menor.")

    if tentativa == max_tentativas - 1:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

print("Fim do jogo!")

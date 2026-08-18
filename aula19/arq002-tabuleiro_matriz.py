








linha = int(input("digite a linha (1,2,3)")) - 1
coluna = int(input(""digite a coluna (1,2,3)"")) -1

if tabuleiro[linha][coluna] != "-":
    print("\n Posição ja ocupada! Tente denovo.")
    continue

tabuleiro[linha][coluna] = jogador
jogadas += 1

# -------------- verificação de vitoria:
# 1- checando as tres linhas.

for l in range(3):
    if batuleiro[l][0] == jogador and tabuleiro [l][1] == jogador and tabuleiro [l][2] == jogador:
        ganhou = True

# ----------------- checando as colunas.
for c in range(3):
    if batuleiro[0][c] == jogador and tabuleiro [1][c] == jogador and tabuleiro [2][c] == jogador:
        ganhou = True

# -------------- checando a diagonal principal.

if batuleiro[0][0] == jogador and tabuleiro [1][1] == jogador and tabuleiro [2][2] == jogador:
        ganhou = True

if batuleiro[0][2] == jogador and tabuleiro [1][1] == jogador and tabuleiro [2][0] == jogador:
        ganhou = True

if ganhou:
     print("Parabens, você GANHOUUU! ")


## ----------------- alterna a jogada se ninguem venceu!

if jogador == "x":
    jogador = "o"
else:
    jogador == "x"

if not ganhou:
    print("".join(linha))
    print(f"\Deu velha! o tabuleiro acabou.")


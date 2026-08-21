

tabuleiro = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]

jogador = 'X'
jogadas = 0
ganhou = False

while jogadas < 9 and not ganhou:
    print("\nTabuleiro Atual:")
    for linha in tabuleiro:
        print(' '.join(linha))

    print(f"\nVez do jogador: {jogador}")

    linha = int(input("Digite a linha (0, 1 ou 2)"))
    coluna = int(input("Digite a coluna (0, 1 ou 2)"))

    if tabuleiro[linha][coluna] != '-':
        print("\n Posição já ocupada! Tente novamente.")
        continue

    tabuleiro[linha][coluna] = jogador
    jogadas = jogadas + 1

    # -------- VERIFICAÇÃO DE VITORIA

    # 1. Checar as 3 linhas
    for l in range(3):
        if tabuleiro[l][0] == jogador and tabuleiro[l][1] == jogador and tabuleiro[l][2] == jogador:
            ganhou = True

    # 1. Checar as 3 colunas
    for c in range(3):
        if tabuleiro[0][c] == jogador and tabuleiro[1][c] == jogador and tabuleiro[2][c] == jogador:
            ganhou = True

    # 3. Checar a diagonal principal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        ganhou = True

    # 4. Checar a diagonal secundaria
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            ganhou = True

    if ganhou:
        print("\n=================================")
        for linha in tabuleiro:
            print(' '.join(linha))
        print(f"\nParabéns! O jogador '{jogador}' VENCEU!")
        break

    # Alterna a jogado caso ninguem tenha vencido
    if jogador == 'X':
        jogador = 'O'
    else:
        jogador = 'X'

if not ganhou:
    for linha in tabuleiro:
        print(' '.join(linha))
    print(f"\Deu velha! O tabuleiro foi completamente preenchido!")
# Mattrizes -

#lista
alunos = ["pedro","antonio","maria","pamela"]


#print(alunos[0])

#como criar uma matriz simples

# #notas = [
#     [8, 7, 10, 9],
#     [5, 6, 7, 8],          #matriz 4x3.
#     [10, 9, 8, 7],
# ]

#print(notas)

#for notas in notas:
#    print(notas)

#print(notas[1][3])



# funcionarios = [
#      ["pedro", 1500, 0.30],
#      ["antonio", 2000, 0.20],
#      ["maria", 3000, 0.1, 0.2],
#      ["pamela", 4000, 0.10]
#  ]

# print(funcionarios[3][1])
# print(funcionarios[2][2])

#pamela = funcionarios[3][1]
#maria = funcionarios[2][2]

#print(f"o salario da pamela é: {pamela} e o valor extra que a lurde vai receber é: {maria}")


## atualizando valores em uma matriz

# print("o salario atual é: ", funcionarios[0][1])
# funcionarios[0][1] = 1501
# print("O salario apos a promocao sera: ", funcionarios[0][1])
#print(funcionarios)



## Percorres matrizes
## percorrer apenas linhas

#for linha in funcionarios:
#    print(linha)


## percorrer cada valor dentro de cada linha

# for linha in funcionarios:
#     for valor in linha:
#         print(valor)


# notas = [
#     [7, 9],
#     [4.500, 1],
#     [1.500, 0]
# ]

# for linhas in notas:
#     for valor in linhas:
#         print(valor + 1)


# calcular em matriz: boletim escolar.


# boletim = [
#      ["pedro", 10, 10, 10],
#      ["antonio", 8, 9, 9],
#      ["maria", 5, 6, 6],
#      ["pamela", 1, 3, 5]
#  ]
# for indice, nota in enumerate(notas):
#     media = sum(nota) / len(nota)
#     maior = max(nota)
#     menor = min(nota)

#     if media > 7:
#          status = "aprovado"
#     else:
#          status = "Reprovado"
#         print(f"Aluno {indice + 1}")
#         print(f"Media: {media:.2f}")
#         print(f"Maior nota: {maior}")
#         print(f"Menor nota: {menor}")
#         print(f"Status: {status}")
#         print("-" * 20)


# tabuleiro = [
#     ["-", "-", "-", ],
#     ["-", "-", "-", ],
#     ["-", "-", "-", ]
# ]


# tabuleiro[1][1] = "X"

# for linha in tabuleiro:
#     print(" ".join(linha))



# Vagas de estacionamento:


vagas = [
    ["L","L","L","L","L"],
    ["L","L","L","L","L"],
    ["L","L","L","L","L"],
    ["L","L","L","L","L"],
    ["L","L","L","L","L"]
]



while True:
    print("\n ==== ESTACIONAMENTO ====")
    print("1 - Vagas")
    print("2 - reservar vaga")
    print("3 - liberar vaga")
    print("4 - sair")

    opcao = input("Qual opçao deseja? ")

    if opcao == "1":
        for linha in vagas:
            print("".join(linha))
    elif opcao == "2":
        linha = int(input("Digite a linha de 1 a 5: "))-1
        coluna = int(input("Digite a coluna de 1 a 5: "))-1

        if vagas[linha][coluna] == "L":
            vagas[linha][coluna] = "O"
            print("Vaga reservada com sucesso!")
        else:
            print("Vaga já ocupada.")
    elif opcao == "3":
        linha = int(input("Digite a linha de 1 a 5: "))-1
        coluna = int(input("Digite a coluna de 1 a 5: "))-1

        if vagas[linha][coluna] == "O":
            vagas[linha][coluna] = "L"
            print("Vaga liberada com sucesso!")
        else:
            print("Vaga já estava livre.")
    elif opcao == "4":
        print("Encerrando o sistema!")
        break
    else:
        print("Opção invalida!")



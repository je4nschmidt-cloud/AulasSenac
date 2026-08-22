nome = input("digite seu nome: ")
print(nome)





## -------------- CSV. [comma separete value]
#- Arquivos de textos simples que utiliza um delimitador para especificar o inicio e o fim de um dado.
# nome,cpf,numcel
#      - mais rapido
#      - mundialmente utilizado para conversar entre sistemas.

#id,nome,cargo
##1,"joao","analista".

from pathlib import Path
import csv
import json

pasta_downloads = Path.home() / "Downloads"
caminho_csv = pasta_downloads / "funcionario.csv"
caminho_json = pasta_downloads / "funcionario.json"


with open(
    "funcionarios.csv",
    "w",#modo modificação: "w" // #modo leitura: "r" // e modo append: "a"
    newline="",
    encoding="utf-8"   #preserva os caracteres especiais.
) as arquivo:
    print("O arquivo está neste bloco.")


## --------- CRUD NO CSV:

######## CREAT:
from pathlib import Path
import csv

#criando dados para aplicação:

funcionarios = [
    [1,"joao","analista","5000"],
    [2,"maria","gerente","8000"],
    [3,"pedro","assistente","2500"]
] 

# with open(
#     caminho_csv,
#     "w",
#     newline="",
#     encoding="utf-8",
# ) as arquivo:

#     escritor = csv.writer(arquivo)

#     escritor.writerow([
#         "id",
#         "nome",
#         "cargo",
#         "salario",
#     ])

#     for funcionario in funcionarios:
#         escritor.writerow(funcionario)

# print("Arquivo criado e o local é: ", caminho_csv)


################ READING: 



# with open(
#     caminho_csv,
#    "r",
#     encoding="utf-8",
# ) as arquivo:

#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)


######### READ COM BUSCA:

# id_procurado = input("Digite um ID")

# with open(
#     caminho_csv,
#    "r",
#     encoding="utf-8",
# )   as arquivo:

#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         if linha[0] == id_procurado:
#             print(linha)



############# UPDATE:


# id_procurado = input("Digite um ID")
# dados = []
# novo_cargo = input("novo cargo desta pessoa: ")

# with open(
#     caminho_csv,
#     "r",
#     encoding="utf-8",
# )   as arquivo:

#     leitor= csv.reader(arquivo)

#     for linha in leitor:
#         if linha[0] == id_procurado:
#             linha[2] = novo_cargo

#             dados.append(linha)

# with open(caminho_csv,"w",newline="",encoding="utf-8") as arquivo:
#     escritor = csv.writer(arquivo)

#     for linha in dados:
#         escritor.writerow(linha)

# print("Atualizando o valor no arquivo: ", caminho_csv)


########### DELET:
dados = []
id_excluir = input("Digite o ID a ser excluido:")


with open(
    caminho_csv,
    "r",
    encoding="utf-8",
)   as arquivo:

    leitor = csv.reader(arquivo)
    for linha in leitor:
        if linha[0] != id_excluir:
            dados.append(linha)
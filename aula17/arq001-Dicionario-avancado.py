# cliente = {
#     "nome": "maria",
#     "idade": 30,
#     "endereco": {
#         "cidade": "porto alegre",
#         "estado": "RS"
#     }
# }

# print(cliente["endereco"]["estado"])



funcionario = {
    "nome": "",
    "cargo": "",
    "matricula": "",
    "hierarquia": {
        "diretoria": "",
        "gerencia": "",
    }
}

funcionario["nome"] = input("Qual seu nome? ")
funcionario["cargo"] = input("Qual seu cargo? ")
funcionario["matricula"] = input("qual sua matricula? ")
funcionario["hierarquia"]["diretoria"] = input("digite a diretoria:")
funcionario["hierarquia"]["gerencia"] = input("digite a hierarquia:")

print(funcionario)





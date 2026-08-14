# Uma lista dentro de um dicionario.

#listas de dicionarios: 

# cliente1 = {
#     "nome": "joao",
#     "cpf": "123456"
# }

# cliente2 = {
#     "nome": "maria",
#     "cpf": "234567"
# }

# cliente1 = {
#     "nome": "jose",
#     "cpf": "345678"
# }

# clientes = [
#     {"nome": "joao", "cpf": "123456"},
#     {"nome": "maria", "cpf": "234567"},
#     {"nome": "jose", "cpf": "345678"}
#     ]

# for cliente in clientes:
#     print(cliente["nome"])



# produto = [
#     {"nome": "morango","preço":"10.50","estoque":"100"},
#     {"nome": "carne","preço":"50.00","estoque":"50"},
#     {"nome": "pao","preço":"15.90","estoque":"30"}
# ]
# for produtos in produto:
#     print(produtos["nome"], ":", produtos["preço"])






# cliente = {
#     "nome": "maria",
# }

# #print(cliente["telefone"]) #forma errada.
# #print(cliente.get("telefone"))

# telefone = cliente.get(
#     "telefone.",
#     "Não informado."
# )
# print(telefone)


# if telefone in cliente:
#     print("Telefone nao existe")
# else:
#     print("o telefone pesquisado nao existe.")



# correntista = {
#     "nome": "joao",
#     "cartao": "1568574"
# }

# if "cartao" in cliente:
#     print("possui cartao")
# else:
#     print("nao possui cartao")

# if "cartao" in correntista:
#     print("possui cartao")
# else:
#     print("nao possui cartao")



# Dicionario contador - 

vendas = [
    "notebook",
    "mouse",
    "notebook",
    "mouse",
    "pendrive",
]

contador = {}

for produto in vendas:
    if produto in contador:
        contador["prdouto"] += 1
    else:
        contador[produto] = 1

print(contador)
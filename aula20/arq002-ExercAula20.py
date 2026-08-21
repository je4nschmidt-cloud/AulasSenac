#EXERCICIO 1


# meus_int = {"musica", "cinema", "tecnologia", "viagens"}
# perfis = [
#     {},
#     {},
#     {},
#     {},
#     {},
# ]

# #menu
# print("\n=== Sistema de MATCH ===")
# print("1 - Ver todos os perfis e compatibilidades.")
# print("2 - Filtrar perfis por compatibilidade.")
# opcao = input("digite a opcao")

# if opcao == "1":
#     print("\n --- Resultado geral ---")
#     for pessoa in perfis:
#         em_comum = meuPeril & pessoa[]




# elif == "2":
#     print("\nFiltrar por faixa")
#     print("1 - até 30% - pouca afinidade")
#     print("2 - De 31 até 70% - match parcial")
#     print("3 - acima de 70% - Match perfeito")
#     faixa = input("escolha a faixa desejada:")

#     encontrou = False

#     print("\n --- Resultados da bunca ---")
#     for pessoa in perfis:
#         em_comum = meus_int & pessoa["interesses"]
#         total = meus_int | pessoa["interesses"]
#         match = (len(em_comum) / len(total)) * 100

#         if faixa == "1" and match <= 30:
#             print(f"- {pessoa["nome"]}: {match:.1f}% de compatibilidade")

#         elif faixa == "2" and 31 <= match <= 70:
#             print(f"- {pessoa["nome"]}: {match:.1f}% de compatibilidade")

#         elif faixa == "3" and match >= 70:
#             print(f"- {pessoa["nome"]}: {match:.1f}% de compatibilidade")
#             encontrou = True

#     if not encontrou:
#         print("")

# else:




#EXERCICIO 2:


catalago = {
    "notebook gamer": {"gamer","portatil","caro","nvidia"},
    "pc office": {"office","barato","desktop","nvidia"},
    "monitor gamer": {"gamer","periferico","caro","promocao"},
    "teclado": {"gamer","portatil","barato","promocao"},
    "mouse": {"gamer","portatil","caro"},
}

print("+" * 30)
print("Produtos em promoção:")
print("+" * 30, "\n")


filtros_usuario = {"gamer","promocao"}

for nome_produto, tag in catalago.items():
    if filtros_usuario.issubset(tag):
        print(f"Produtos encontrados: {nome_produto}")
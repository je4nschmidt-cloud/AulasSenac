
                           ## Desafio: Expedição às ruinas de Aethel.##
## Você foi contratado oara desenvolver o sistema de software da corporação Aethel, uma guilda responsável por enviar exploradores as ruínas antigas.
## O seu programa será a ferramenta que o explorador leva em seu terminal portátil duranre as missões. Ele deve gerenciar o cadastro do aventureiro, 
## controlar os itens encontrados, simular os imprevistos do dia a dia da expedição e gerar um relatório final completo ao término da jornada.



import random   
import numpy as np

dias = 0

locais_exp = ()
taxas_guild = ()

explorador = {
    "nome": "",
    "ouro": 0.0,
    "dias_exp": 0,
}
# dicionario com try letras no lugar de numeros.

bag = [
    ["V","V","V","V","V",],
    ["V","V","V","V","V",],
    ["V","V","V","V","V",],          #bag 5x5.
    ["V","V","V","V","V",],
    ["V","V","V","V","V",],
]

print("Olá, explorador(a) seja bem-vindo!")

while True:
    try:
        explorador["nome"] = str(input("Digite seu nome explorador(a):"))
        explorador["ouro"] = float(input("Digite quanto ouro tem:"))
        explorador["dias_exp"] = int(input("Qual é o seu dia de exploração?"))
        print("Sua aventura começa agora! Aqui vão suas informações.")
        print(explorador)
        break
    except ValueError:
            print("informação invalida. Insira um valor válido")

print(f"Boa sorte, {explorador['nome']} nessa aventura.")
print("Como boas vindas, você vai receber alguns itens: Bolsa com 100 moedas e uma bussúla.")
bag[0][0] = "bag_de_moedas"
bag[0][1] = "bussúla"
for lista in bag:
    print(lista)

explorador["ouro"] = 100.00
print(explorador)
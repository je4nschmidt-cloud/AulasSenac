### ----------- REVISAO COMENTADA:

### ESTRUTURA DE DADOS: São recursos/objetos presentes no python, que são utilizados para armazemento e manipulaçao de dados em memoria.

##LISTAS: Coleção heterogenea (varios tipos de dados), mutavel (pode ser alterada) e deve ser utilizada quando voce alterar, remover e adicionar itens dinamicamente por indice ou valor.

## -------- CRUDI:

#CRIANDO UMA LISTA [CREATING]:
nome_da_lista = [] #criando uma lista vazia
nome_da_lista_c_valores = ["big mac",29.90,120,"29-05-2026"] #criando uma populada ou com valores

#LENDO OU APRESENTANDO UMA LISTA [READING]:
print(nome_da_lista_c_valores)

#ATUALIZANDO UM VALOR DENTRO DA LISTA [UPDATEING]:
nome_da_lista_c_valores[0] = "mc melt"

#REMOVENDO UM VALOR DA LISTA [DELETE]:
nome_da_lista_c_valores.remove("mc melt") #ou por indice

# INSERINDO UM VALOR NA LISTA [INSERT]:
nome_da_lista_c_valores.append("mc melt")


##TUPLAS: Coleção heterogenea (varios tipos de dados), imutavel (nao pode ser alterada) e deve ser utilizada quando voce possui dados que nao podem ser alterados(CPF, LOCALIZACAO EM COORDENADAS, CEP E ETC).

#criando uma tupla:
nome_da_tupla = (1234, 2345, 3456)

#lendo ou apresentando um tupla:
print(nome_da_tupla)

##DICIONARIO: É uma coleção de dados mapeados com chave e valor. Os dicionarios eles sao heterogeneos, mutaveis e devem ser utilizados para representar entidades do mundo real.

#CRIANDO UM DICIONARIO:
nome_do_dicionario = {}
nome_do_dicionario_c_valor = {
    "chave1":"valor1",
    "chave2": 1000,
}

#LENDO UM DICIONARIO:

print(nome_do_dicionario_c_valor)
print(nome_do_dicionario_c_valor["chave1"])

# ATUALIZANDO UM VALOR NO DICIONARIO:

nome_do_dicionario_c_valor["chave1"] = "valor2"

# REMOVENDO UM VALOR DO DICIONARIO :

del nome_do_dicionario_c_valor["chave2"]

# INSERINDO UM VALOR NO DICIONARIO:

nome_do_dicionario_c_valor["chave3"] = "valor3"

## ------ DICIONARIOS ANINHADOS:

nome_do_dicionario_aninhado = {}
nome_do_dicionario_aninhado_c_valor = {
    "nome lanche":"bigmac",
    "valor":30.00,
    "ingredientes":{
        "tipo carne":"gado",
        "saladas":{
            "salada1":"alface",
            "salado2":"tomate",
            "salada3":"picles",
        },
        "molho":"molho especial",
    }
}

print(nome_do_dicionario_aninhado_c_valor)


# ATUALIZANDO UM VALOR NO DICIONARIO ANINHADO:

nome_do_dicionario_aninhado_c_valor["ingredientes"]["saladas"]["salada1"] = "rucula"

## -------------- ARRAY : Também consegue receber um CRUDI completo.

import numpy as np

notas_array = np.array([1,2,3,4,5])
print((notas_array * 2) + 1)

print("A soma dos valores do array é: ", notas_array.sum())
print("A media dos valores do array é: ", notas_array.mean())
print("O maior valores do array é: ", notas_array.max())
print("O Menor valores do array é: ", notas_array.min())

resultado = notas_array[notas_array < 3]
print(resultado)

## ------------------------

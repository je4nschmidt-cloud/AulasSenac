import random # a funcao random é usada para gerar numeros aleatorios.

for i in range(5):
   print(random.random()) # Imprime um número aleatório entre 0 e 1


for u in range(5):
   print(random.randint(1, 10)) # Imprime um número aleatório entre 1 e 10


for e in range(5):
   print(random.uniform(1, 10)) # Imprime um número aleatório entre 1 e 10


# imprima os valores entre 5 e 10, apartir do input do usuario. usando while.

num = int(input("Digite um número: "))
i = 5
while i < num or i == num:
    print(i)
    i += 1

#imprima os valores impares entre 1 e 10, usando for.

for i in range(1, 11):
    if i % 2 != 0:
        print(i)



# imprima os valores do nome do usuario, usando while.

nome = input("Digite seu nome: ")
indice = 0
while indice < len(nome):
    print(nome[indice])
    indice += 1



# imprima o nome do usuario de tras para frente, usando while.

nome_ = input("Digite seu nome: ")
i = len(nome_) - 1
while i >= 0:
    print(nome_[i], end="")
    i -= 1


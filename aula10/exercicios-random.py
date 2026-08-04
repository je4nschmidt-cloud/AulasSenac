import random
qtd_num = 0
while qtd_num <= 5:
    print(random.random()) # Imprime um número aleatório entre 0 e 1
    qtd_num += 1


qtd_num2 = 0
while qtd_num2 <= 5:
    print(random.randint(1, 10)) # Imprime um número aleatório entre 1 e 10
    qtd_num2 += 1


#imprima um numero de 10 a 100.

import random

print(random.randint(10, 100)) # Imprime um número aleatório entre 10 e 100



#imprima os valores anteriores a um numero digitado.

num = int(input("Digite um número: "))
i = 0
while i < num:
    print(i)
    i += 1
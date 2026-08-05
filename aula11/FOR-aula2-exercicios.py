# #1. Escreva um loop for que imprima os números de 1 a 10.

# for i in range(1, 11):
#     print(i)

# #2. Escreva um loop while que imprima os números de 1 a 10.

# i = 0
# while i < 10:
#     i += 1
#     print(i)

# #3. Escreva um loop for que imprima os números pares de 1 a 20.

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)
# #4. Escreva um loop while que imprima os números pares de 1 a 20.

# i = 0
# while i < 20:
#     i += 1
#     if i % 2 == 0:
#         print(i)
# #5. Escreva um loop for que imprima os números ímpares de 1 a 20.

# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)
# #6. Escreva um loop while que imprima os números ímpares de 1 a 20.

# import random

# i=0
# while i < 20:
#     if i % 2 != 0:
#         print(i)
#     i += 1

#7. Escreva um loop for que calcule a soma dos números de 1 a 10.

# soma = 0
# for i in range(1, 11):
#     soma += i
#     print(soma)


# #8. Escreva um loop while que calcule a soma dos números de 1 a 10.

# soma = 0
# i = 1
# while i <= 10:
#     soma += i
#     i += 1
#     print(soma)


#9. Escreva um loop for que calcule o produto dos números de 1 a 5.

# produto = 1
# for i in range(1, 6):
#     produto *= i
#     print(produto)

# # #10. Escreva um loop while que calcule o produto dos números de 1 a 5.

# produto = 1
# i = 1
# while i <= 5:
#     i += 1
#     produto *= i
#     print(produto)



#10.5. calcular uma fatorial de um numero.
# numero = 5
# fatorial = 1
# for i in range(1, numero + 1):
#     fatorial *= i
# print(f"O fatorial de {numero} é {fatorial}")




#11. Escreva um loop for que imprima os caracteres de uma string.

# string = "cinco"
# for i in string:
#     print(i)




#12. Escreva um loop while que imprima os caracteres de uma string.

# string = "cinco"
# i = 0
# while i < len(string): # ou index <= len(string) -1
#     print(string[i])
#     i += 1

#13. Escreva um loop for que encontre o maior elemento de uma lista.

# lista = [3, 7, 2, 9, 5]
# maior = lista[0]
# for i in lista:
#     if i > maior:
#         maior = i
# print(f"O maior elemento da lista é: {maior}")

#14. Escreva um loop while que encontre o maior elemento de uma lista.

#15. Escreva um loop for que encontre o menor elemento de uma lista.

#16. Escreva um loop while que encontre o menor elemento de uma lista.

#17. Escreva um loop for que conte o número de elementos em uma lista.

#18. Escreva um loop while que conte o número de elementos em uma lista.

#19. Escreva um loop for que inverta uma string.

#20. Escreva um loop while que inverta uma string.

#35. 

tamanho = int(input("Digite o tamanho da arvore: "))

for i in range(1, tamanho + 1):
    espaco = " " * (tamanho - i)
    linha = ""
    j = 1
    while j <= i:
        linha += str(i) + " "
        j += 1
    print(espaco + linha.strip())
# BREAK e CONTINUE - são palavras reservadas utilizadas para controlar o fluxo de execução de loops (laços) em Python.

# lista_numeros = [1,3,7,9,12,15,19,22]

# for num in lista_numeros:
#     if num % 2 == 0:  # Verifica se o número é par.
#         print(f"{num} é par, então vamos achar o proximo par.")  # Mensagem indicando que o número é par.
#         continue  # Pula para a próxima iteração do loop.
#     print(f"{num} é ímpar, então vamos continuar com a execução.")  # Mensagem indicando que o número é ímpar.

# Imprime os numeros impares pulando os pares.

# for i in range(1, 10):
#     if i % 2 == 0:  # Verifica se o número é par.
#         continue  # Pula para a próxima iteração do loop.
#     print(f"{i} é ímpar.")  # Mensagem indicando que o número é ímpar.



## PASS - é uma palavra reservada utilizada para indicar que não há ação a ser executada em um determinado bloco de código.



#criar uma calculadora simples que recebe dois numeros e uma operação, caso a operação seja divisao usar try except para tratar a divisão por zero.

num_1 = float(input("Digite o primeiro número: "))
num_2 = float(input("Digite o segundo número: "))
operacao = (input("Digite a operação (+, -, *, /): "))
resultado = 0

if operacao == "/":
    try:
        resultado = num_1 / num_2
        print(f"{num_1} {operacao} {num_2} = {resultado}")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
else:
    if operacao == "+":
        resultado = num_1 + num_2
    elif operacao == "-":
        resultado = num_1 - num_2
    elif operacao == "*":
        resultado = num_1 * num_2
    else:
        print("Operação inválida.")
    print(f"{num_1} {operacao} {num_2} = {resultado}")
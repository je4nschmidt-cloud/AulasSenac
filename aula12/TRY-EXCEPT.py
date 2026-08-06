
# Try/Except - é um bloco/controle de exceção utilizado para manter a aplicabilidade da ação do sistema mesmo que ocorra algum erro durante a execução do código.

#Garantir que o usuario digite um numero valido:
# try:
#     numero = int(input("Digite um número: "))  # Tenta converter a entrada do usuário para um número inteiro.
#     resultado = 100 / numero  # Tenta realizar a divisão.
#     print(f"100 / por {numero} é igual a {resultado}")  # Exibe o resultado da divisão.
# except ValueError:  # Captura o erro caso a entrada não seja um número inteiro.
#     print("Erro: Você não digitou um número válido.")  # Mensagem de erro para entrada inválida.
# except ZeroDivisionError:  # Captura o erro caso o usuário digite zero.
#     print("Erro: Não é possível dividir por zero.")  # Mensagem de erro para divisão por zero.


# crie uma lista vazia e insira numeros de 1 a 10 com bloco try/except para caso o usuario digite um valor invalido.
# lista_numeros = []  # Cria uma lista vazia para armazenar os números.

# for i in range(1,11):
#     lista_numeros.append(i)

# try:
#     opçao = int(input("Digite um número para verificar se ele está na lista: "))
#     if opçao in lista_numeros:  
#         print(f"O número {opçao} está na lista.")  
#     else:
#         print(f"O número {opçao} não está na lista.")
# except ValueError: 
#     print("Erro: Você não digitou um número válido.")  

# crie uma lista vazia com os numero pares de 2 a 20, porem com varias tentativas antes de sair da execusão do programa.

pares = []

for i in range(2, 21, 2):
    pares.append(i)

#criar um loop para dar 3 chances para o usuario digitar um numero par, caso ele erre 3 vezes, o programa deve encerrar a execução.
for tentativa in range(1, 4):
    try:
        numero = int(input(f"Tentativa {tentativa}. Digite um número par entre 2 e 20: "))
        if numero in pares:
            print(f"Parabéns! O número {numero} é par e está na lista.")
        else:
            print(f"O número {numero} não é par ou não está na lista. Tente novamente.")
    except ValueError:
        print("Erro: Você não digitou um número válido. Tente novamente.")
else:
    print("\nVocê excedeu o número de tentativas. O programa será encerrado.")
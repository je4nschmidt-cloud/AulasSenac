
valor = int(input("Digite um numero: "))

#decisao simples:
if valor > 0:
    print("O valor digitado é positivo.")
if valor < 0:
    print("O valor digitado é negativo.")
if valor == 0:
    print("O valor digitado é igual a zero.")

#decisao encadeada:
if valor > 0:
    print("O valor digitado é positivo.")
elif valor < 0: 
    print("O valor digitado é negativo.")
else:
    print("O valor digitado é igual a zero.")

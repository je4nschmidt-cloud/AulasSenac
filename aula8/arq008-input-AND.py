
valor = int(input("Digite um valor inteiro: "))

if valor > 0 and  valor % 2 == 0:
    print("o valor é positivo e par.")
elif valor > 0 and valor % 2 == 1:
    print("o valor é positivo e ímpar.")
elif valor < 0 and valor % 2 == 0:
        print("o valor é negativo e par.")
elif valor < 0 and valor % 2 == 1:
        print("o valor é negativo e ímpar.")
else:
        print("zero nao é positivo nem negativo e nem par nem ímpar.")
        
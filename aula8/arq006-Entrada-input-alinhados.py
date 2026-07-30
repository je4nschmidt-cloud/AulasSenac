
valor = int(input("Digite um valor inteiro: "))

if valor > 0:
    print("O valor é positivo.")
    if valor % 3 == 0:
        print("O valor é múltiplo de 3.")
    elif valor % 5 == 0:
        print("O valor é múltiplo de 5.")
    else:
        print("O valor não é múltiplo de 3 nem de 5.")
elif valor < 0:
    print("O valor é negativo.")
    if abs(valor) % 7 == 0:
        print("O valor é múltiplo de 7.")
    else:
        print("O valor não é múltiplo de 7.")
else:
    print("O valor é zero e não é múltiplo de nada.")
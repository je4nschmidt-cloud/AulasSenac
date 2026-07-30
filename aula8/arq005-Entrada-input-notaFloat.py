
nota = float(input("Digite a nota do aluno: "))

if nota >= 9.0:
    print("Aprovado com louvor!")
elif nota >= 8.0:
    print("Aprovado com mérito.")
elif nota >= 7.0:
    print("Aprovado.")
elif nota >= 6.0:
    print("Aprovado com ressalvas.")
else:
    print("Reprovado.")
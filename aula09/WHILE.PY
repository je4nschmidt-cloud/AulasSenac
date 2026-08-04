#WHILE - Estrutura de repetição com condição.

qtd_alunos = 0

while qtd_alunos < 10:
  print(f"Quantidade de alunos: {qtd_alunos}")
  qtd_alunos += 1

# looping com determinada condição. pode ter condicionais.

qtd_alunos2 = 0

while qtd_alunos2 < 11:
  if qtd_alunos2 % 2 == 0:
    print(f"o numero: {qtd_alunos2} é par.")
  else:
    print(f"o numero: {qtd_alunos2} é impar.")
  qtd_alunos2 += 1
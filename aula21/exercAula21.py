#Exercício 1 (Pilha): Editor de Texto - Função Ctrl+Z 
#Crie um programa que simule as ações de um usuário digitando em um editor. 
#Crie uma pilha vazia chamado texto. 
#Adicione as seguintes ações sequenciais: "Texto 1", "Texto 2", "Texto 3". 
#Simule o usuário apertando Ctrl+Z duas vezes (removendo as duas últimas ações). 
#Imprima o estado final do texto na tela. 


texto = []

texto.append("texto 1")
texto.append("texto 2")
texto.append("texto 3")

print(texto)

print("apertando crtl+z primeira vez.")
texto.pop()
print("apertando crtl+z segunda vez.")
texto.pop()

print(texto)

# Exercício 2 (Fila): Sistema de Suporte Técnico 
# Crie um sistema para gerenciar chamados de TI. 
# Crie uma fila de atendimento contendo 3 chamados: "Erro no Monitor", "Troca de Senha", "Sem Internet". 
# O sistema deve ter um loop (while) que atenda (remova) um chamado por vez, exibindo a mensagem: "Atendendo chamado: [Nome do Chamado]...". 
# O loop deve rodar até que a fila fique completamente vazia. 

from collections import deque

filas_pedidos = deque(["Erro no Monitor", "Troca de Senha", "Sem Internet"])

print(" --- INICIANDO ATENDIMENTOS DE SUPORTE --- ")
while len(filas_pedidos) > 0:
    chamado_atual = filas_pedidos.popleft()
    print(f"Atendendo ao chamado: {chamado_atual}")

print("\n --- todos chamados foram atendidos!")
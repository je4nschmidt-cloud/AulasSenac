# STACKS - PILHAS.
# QUEUES - FILAS.

#SIMULAÇÃO DO HISTORICO DE NAVEGADOR - APLICANDO PILHAS [ LIFO ]

historico_abas = []

# O USUARIO VAI CLICANDO E ABRINDO PAGINAS [ EMPILHANDO PAGINAS]. 

print("Navegando pela web")

historico_abas.append("google.com")
historico_abas.append("github.com")
historico_abas.append("youtube.com")

print("pagina atual visivel na tela: ", historico_abas[-1])
print("pilha atual: ", historico_abas)
print("_" * 40)

print("1 - clicando no botao de boltar (desempilhando)")
pagina_saindo = historico_abas.pop()
print(f"saindo da pagina: {pagina_saindo}")

# PARA REMOVER TEMOS : REMOVE() , DISCARD(), DEL(), POP().

# ONDE O USUARIO ESTA AGORA:
print("onde o usuario está agora: ")
print("nova pagina atual: ", historico_abas[-1])
print("pilha atualizada: ", historico_abas)

############################ ------------------------------------


from collections import deque  # OTIMIZA FILAS

filas_pedidos = deque()

# chegada de pedidos no sistema
print("chegada de novos pedidos no balcao.........")
filas_pedidos.append("pedido #101: x-burgues")
filas_pedidos.append("pedido #120: batata")
filas_pedidos.append("pedido #130: refri")

print("\nFila atual de espera: ", list(filas_pedidos))

print("\nCozinha chamado para preparo")
pedidos_em_preparo = filas_pedidos.popleft()
print(f"Preparando agora: {pedidos_em_preparo}")

print("\nProximo da fila a ser preparado: ", filas_pedidos[0])
print("Fila restante", list(filas_pedidos))

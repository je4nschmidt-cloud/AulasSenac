# listas sao feitas com colchetes e os elementos sao separados por virgula

planetas = ["Terra", "Marte", "Jupiter", "Saturno"]
print(planetas[0]) # imprime o primeiro elemento da lista
print(planetas) #   imprime a lista completa
# planetas.append("Urano") # adiciona um elemento no final da lista
# planetas.insert(1, "Venus") # adiciona um elemento em uma posicao especifica
# planetas.remove("Jupiter") # remove um elemento da lista
# planetas.pop() # remove o ultimo elemento da lista
# planetas.sort() # ordena a lista em ordem alfabetica
# planetas.reverse() # inverte a ordem da lista
# planetas.clear() # limpa a lista

primeiro_planeta = planetas[0] # acessa o primeiro elemento da lista
print(primeiro_planeta)


for planeta in planetas:
    print(planeta) # percorre a lista e imprime cada elemento




numeros = [3, 10, 4, 10, 12]
print(numeros) # imprime a lista completa
numeros_ordenados = numeros.sort() # ordena a lista em ordem crescente
print(numeros) 
ocorrencias = numeros.count(10) # conta quantas vezes o numero 10 aparece na lista
print(ocorrencias) # imprime o numero de ocorrencias do numero 10 na lista
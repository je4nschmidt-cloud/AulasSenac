# o que é uma ARRAY? - é uma sequencia continua na memoria ram, reservada para guardar dados
#do mesmo tipo (homogeneos).

#Por que usar ARRAY? e não LISTA? - A lista guarda ponteiros (endereços) apontados para objetos espalhados na memoria ram.
# o array junta tudo em unico bloco continuo, economizando memoria e aumentando a performance.

#Quando utilizar um e outro? - 

# Use lista, quando precisar misturar tipos de dados, mudar o tamanho a todo momnento, ou criar coleções simples.

#Use ARRAY! - quando for trabalhar exclusivamente com numeros. (EX: Processamento de dados, sinais, imagens, graficos e etc) e quando precisar de desempenho.


#Array nativo: Se voce precisa de performance e economizar memoria, o modulo nativo do array obriga todos os elementos a serem do mesmo tipo (EX: apenas inteiros ou decimais).

# import array
# "i" faz com que esse array aceite apenas numeros INTEIROS.
# vetores_inteiros = array.array("i", [10, 20, 30, 40])
# print(" array de inteiros: ", vetores_inteiros)
# print("O valor presente no indice 0: ", vetores_inteiros[0])

# try:
#     vetores_inteiros.append("AB")
# except TypeError as e:
#     print("\nErro de tipagem: O array bloqueou a inserção")
#     print("Motivo:", e)



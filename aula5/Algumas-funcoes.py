# ALGUMAS FUNÇÕES NATIVAS DO PYTHON

print(pow(2,10))
# A função "pow()" realiza a pontencia de um numero sobre o outro

a = pow(3,2)
print(a)

print(abs(-11))
# a funcao "abs()" retorna o valor absoluto de um numero

quociente, resto = divmod(5,3)
print(resto)
print(quociente)
# a funcao "divmod()" retorna o quociente e o resto da divisao

print(bin(513))
# a funcao "bin()" converte um numero para a base binaria

print(oct(80))
# a funcao "oct()" converte um numero para base octal

print(hex(777))
# a funcao "hex()" converte um numero para a base hexadecimal

print(round(3.14152832, 2))
print(round(3.14152832, 1))
# funcao que arredonda valores com ponto flutuante

import math
# importando a classe matematica

print(math.ceil(4.1))
# arredondamento para cima

print(math.floor(5.9))
# arredonda para baixo

print(math.fabs(-5.4))
# retorna um valor absoluto do float

print(math.factorial(5))
# retorna o fatorial

print(math.fmod(5, 4))
# retorna o resto da divisao como float

print(math.trunc(5.2))
# trunca um numero retornando um inteiro

print(math.pow(2,9))
# eleva o primeiro numero ao segundo

print(math.sqrt(2))
# retorna a raiz quadrada

print(math.pi) # valor de pi
print(math.e) # valor de euler
# valores especiais
print(math.exp(4))
# euler elevado a n

print(math.log(1000,10))
# retorna o logaritimo de um numero por outro
print(math.log10(1000))
# retorna o log 10 de um numero

help(print)
# help() é uma ferramente nativa (built-in) do python usada para acessar o sistema de documentacao e ajuda da linguagem


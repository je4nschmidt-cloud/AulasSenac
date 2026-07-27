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

grito = "AEEEEEEEEEEEEEEEEEEEEE"
print(grito.upper()) #deixa todas as letras maiusculas
print(grito.lower()) #deixa todas as letras minusculas
print(grito.capitalize()) #deixa a primeira letra maiuscula
print(grito.title()) #deixa a primeira letra de cada palavra maiuscula
print(grito.strip()) #remove os espacos em branco do inicio e do fim da string
print(grito.replace("A", "O")) #substitui uma letra por outra  
print(grito.split("E")) #divide a string em uma lista de strings, usando o caractere especificado como delimitador
print(grito.find("E")) #retorna o indice da primeira ocorrencia do caractere especificado na string
print(grito.count("E")) #retorna o numero de ocorrencias do caractere especificado na string
print(grito.startswith("A")) #retorna True se a string comecar com o caractere especificado, caso contrario retorna False
print(grito.endswith("E")) #retorna True se a string terminar com o caractere especificado, caso contrario retorna False
print(grito.isalpha()) #retorna True se todos os caracteres da string forem alfabeticos, caso contrario retorna False
print(grito.swapcase()) #inverte a capitalizacao de todas as letras da string  
print(grito.isdigit()) #retorna True se todos os caracteres da string forem digitos, caso contrario retorna False
print(grito.islower()) #retorna True se todos os caracteres da string forem minusculos, caso contrario retorna False
print(grito.isupper()) #retorna True se todos os caracteres da string forem maiusculos, caso contrario retorna False
print(grito.isspace()) #retorna True se todos os caracteres da string forem espacos em branco, caso contrario retorna False
print(grito.isalnum()) #retorna True se todos os caracteres da string forem alfanumericos, caso contrario retorna False
print(grito.isprintable()) #retorna True se todos os caracteres da string forem imprimiveis, caso contrario retorna False
print(grito.isidentifier()) #retorna True se a string for um identificador valido, caso contrario retorna False
print(grito.isnumeric()) #retorna True se todos os caracteres da string forem numericos, caso contrario retorna False

espacos = '-','   espaçoso   ','-'
print(espacos)
print('-','   tirando    '.strip(),'-')

print('-','   espaço    '.rstrip(),'-') #remove os espacos em branco do final da string
print('-','   espaço    '.lstrip(),'-') #remove os espacos em branco do inicio da string

texto = "Um anel para todos governar, um anel para encontrá-los, um anel para a todos trazer e na escuridão aprisioná-los"
print(texto.replace('anel', 'anelzinho')) #substitui uma palavra por outra dentro da string(print)




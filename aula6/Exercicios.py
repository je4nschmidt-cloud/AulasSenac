#EXERCÍCIOS:

#1) Crie uma variável txt contendo a string "aula5" e verifique, utilizando o método isalnum(), se todos os seus caracteres são alfanuméricos (letras ou números). Exiba o resultado booleano.
txt = "aula5"
x = txt.isalnum()
print(x)

#2)  Crie uma variável tyt contendo uma string formada apenas por espaços em branco e utilize o método isspace() para verificar se a string é composta exclusivamente por espaços. Exiba o resultado.
tyt= "     "
print(tyt.isspace())


#3)  Converta o número de ponto flutuante 3.14 para o tipo inteiro utilizando a função int() e exiba o resultado, observando que a parte decimal será descartada (truncada).
pi = 3.14
print(int(pi))

#4) Atribua o valor '42' (como string) à variável valor e exiba o seu tipo de dado utilizando a função type().
valor = '42'
print(type(valor))


#5) Converta a variável valor, que anteriormente era uma string, para o tipo inteiro utilizando a função int() e exiba o novo tipo de dado para confirmar a conversão.
valor = '42'
valor = int(valor)
print(valor)

#6) Atribua o valor inteiro 3 à variável p e exiba o seu conteúdo na tela.
p = 3
print(p)

#7)  Converta a string '3.14' para o tipo de ponto flutuante (float) e exiba o tipo de dado da variável resultante p2.
p2 = '3.14'
p2 = float(p2)
print(type(p2))

#8) Dadas duas variáveis n1 e n2 contendo os valores '3.5' e '1.7' como strings, converta-as para float, realize a soma e exiba o resultado formatado como 3.5 + 1.7 = <resultado>.
n1 = '3.5'
n2 = '1.7'
n1 = float(n1)
n2 = float(n2)
resultado = n1 + n2
print("3.5 + 1.7 = ", resultado)

#9) Converta o número inteiro 42 para o tipo string utilizando a função str() e exiba o tipo de dado da variável resultante c.
c = 42
c = str(c)
print(type(c))

#10) Converta o número de ponto flutuante 3.14 para string, armazene-o na variável c1 e, em seguida, exiba tanto o valor quanto o tipo de dado da variável.
c1 = 3.14
c1 = str(c1)
print(c1, type(c1))

#11) Dadas as variáveis um (string '1') e um1 (inteiro 1), tente realizar a operação de soma/concatenação entre elas com print(um + um1). Observe que ocorrerá um erro do tipo TypeError, pois o Python não permite concatenar diretamente uma string com um inteiro — seria necessário converter um dos operandos para o tipo do outro antes da operação.
um = '1' 
um1 = 1
print(um + um1)

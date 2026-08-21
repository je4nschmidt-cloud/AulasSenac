#------------------ Conjuntos ou Set:


# LISTA vs SET:
#LISTA: obedece a ordem de chegada e nao elimina as duplicatas.
#SET: ignora a ordem de cehgada e elimina os repetidos, reoganizando os dados internamente.

import time

# 1---- criando lista
cadastro_lista = []
contador = 0

while contador < 500000:
    cadastro_lista.append(contador)
    contador += 1
# 2------ criando set

cadastro_set = set(cadastro_lista)

# 3------------- lista de 1000 ID's que queremos consultar se existe.

ids_consultar = list(range(40000, 50000))

print("base de dados carregado!\n")


# ---------- teste 1 - medindo o tempo de busca na lista
print("iniciando a busca na lista")

inicio_lista = time.time()

encontrados_lista = []
for id_busca in ids_consultar:
    if id_busca in cadastro_lista:
        encontrados_lista.append(id_busca)

fim_lista = time.time()

tempo_lista = fim_lista - inicio_lista
print(f" --> tempo total de busca na lista: {tempo_lista:.4f} segundos. ")



# ---------- teste 2 - medindo o tempo de busca no set


inicio_set = time.time()

encontrados_set = []
for id_busca in ids_consultar:
    if id_busca in cadastro_set:
        encontrados_set.append(id_busca)

fim_set = time.time()

tempo_set = fim_set - inicio_set

print(f" --> tempo toral de busca no set: {tempo_set:.6f} segundos.")


# comparativo final:

print(f"busca na lista: {tempo_lista:.4f} segundos.")

print(f"busca no set: {tempo_set:.6f} segundos.")

vezes_mais_rapido = tempo_lista / tempo_set
print(f"\nO junto (Set) foi mais rapido {vezes_mais_rapido} que a Lista.")


# ------------- Operadores
# & Interseção - Acha o que esta presente nos dois.
# - Diferença: Acha o que tem no primeiro, menos o que tem no segundo.
# | Uniao: Junta tudo sem repetir nada.
# ^ Diferença Semantica: Encontra o que exclusivo de cada um.

candidato = {"python", "sql", "Docker","GiT","HTML"}
#habilidades exigidas para a vaga
requisitos_vaga = {"python", "sql", "Docker","Kubernates","AWS"}

print("=== Analise automatica de correspondeica ===")

#1. Quais requisitos o candidato ja cobre.
requisitos_atendidos = candidato & requisitos_vaga
print("O que ele ja sabe apra a vaga: ", requisitos_atendidos)


#2. o que a vaga pede e o candidato nao tem.
gaps_conhecimento = candidato - requisitos_vaga
print("O que lhe falta: ", gaps_conhecimento)

#3 todas tecnologia envolvidas.
todas_tecnologias = candidato | requisitos_vaga
print("Tecnologias envolvidas na analise: ", todas_tecnologias)




# Set ou {}: Cria um conjuto
# Add(): Insere um item no conjunto
#Discard(): Remove um item sem dar erro caso ele nao existe
#in> Pergunta se um item está no conjunto.

habilidades_candidato = {"python", "sql", "Docker","GiT","HTML"}

habilidades_candidato.add("linux")

print(habilidades_candidato)

habilidades_candidato.discard("GiT")

print(habilidades_candidato)

if "python" in habilidades_candidato:
    print("1")
else:
    print("0")







#Desafio app sugestão de amizades:

minha_rede = {"jean", "bruna", "pedro", "jeff bezos", "elon musk", "neymar"}
rede_joana = {"pedro", "jeff bezos", "elon musk", "soraia", "lula", "bolsonaro"}


meu_nome = "giulio"

print("+" * 30)
print("Algoritomo de recomendações")
print("+" * 30)

conexoes_em_comum = minha_rede & rede_joana
print(f"\nVoce e joana tem {len(conexoes_em_comum)} conexoes em comum")
for pessoa in conexoes_em_comum:
    print(f" - {pessoa}")

sugestao_para_mim = rede_joana - minha_rede - {meu_nome}
print(f"Sugestão para mim: ")
for pessoa in sugestao_para_mim:
    print(f" + Adicionar {pessoa}")



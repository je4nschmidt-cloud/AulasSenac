# Exercício 2 - Controle Acadêmico de Aluno 

# Enunciado 

# Uma instituição de ensino deseja criar um sistema simples para registrar o desempenho de um aluno. 

# O programa deve cadastrar o nome do aluno, o curso e três notas. As notas devem ser armazenadas dentro de uma lista, e essa lista deve fazer parte do dicionário do aluno. 

# Depois do cadastro, o sistema deve calcular a média das três notas e adicionar essa média ao dicionário. 

# Com base na média calculada, o sistema deve definir automaticamente a situação do aluno: 

# Se a média for maior ou igual a 7, a situação será "Aprovado". 

# Se a média for maior ou igual a 5 e menor que 7, a situação será "Recuperação". 

# Se a média for menor que 5, a situação será "Reprovado". 

# Ao final, o programa deve exibir todos os dados do aluno. 

# Caso o usuário digite uma nota inválida, o programa deve mostrar uma mensagem de erro. 

# Requisitos 

# O programa deve: 

# Criar um dicionário chamado aluno. 

# Solicitar:  

# nome do aluno; 

# curso; 

# três notas. 

# Armazenar as notas em uma lista dentro do dicionário. 

# Calcular a média das notas. 

# Adicionar a média ao dicionário. 

# Definir a situação do aluno com if/elif/else. 

# Exibir o cadastro completo usando for e .items(). 

# Utilizar try/except para tratar erro nas notas. 


# aluno = {
#     "nome": input("Digite o nome do aluno: "),
#     "curso": input("Digite o curso do aluno: "),
#     "notas": []
# }

# try:
#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a primeira nota: "))
#     nota3 = float(input("Digite a primeira nota: "))

#     aluno["notas"].append(nota1)
#     aluno["notas"].append(nota2)
#     aluno["notas"].append(nota3)

#     media = sum(aluno["notas"]) / 3
#     aluno["media"] = media

#     if media > 7:
#         aluno["situação"] = "aprovado."
#     elif media > 5:
#         aluno["situação"] = "recuperação."
#     else:
#         aluno["situação"] = "reprovado."
#     print("\nResultado do aluno: ", aluno["situação"])

#     for chave, valor in aluno.items():
#         print(chave,":",valor)
# except:
#     print("ERRO! as notas sempre devem ser numericas.")

 

# Exercício 3 - Sistema de Chamados de TI 

# Uma empresa deseja criar um sistema simples para registrar e acompanhar chamados de TI. 

# O sistema deve permitir que o usuário crie um chamado informando número, solicitante, categoria e prioridade. Todo chamado deve iniciar com o status "Aberto". 

# Depois de criado, o sistema deve apresentar um menu para que o atendente consiga consultar o chamado, alterar a prioridade, alterar o status, remover a categoria, mostrar o chamado completo ou encerrar o programa. 

# Sempre que a prioridade do chamado for "Alta", o sistema deve exibir a mensagem "Atendimento urgente.". 

# O sistema deve continuar funcionando até que o usuário escolha a opção de encerramento. 

# Requisitos 

# O programa deve: 

# Criar um dicionário chamado chamado. 

# Criar um menu com while True. 

# Permitir as seguintes opções:  

# criar chamado; 

# consultar chamado; 

# alterar prioridade; 

# alterar status; 

# remover categoria; 

# mostrar chamado completo; 

# encerrar sistema. 

# Definir o status inicial como "Aberto". 

# Exibir alerta quando a prioridade for "Alta". 

# Usar for e .items() para exibir o chamado completo. 

# Usar try/except ao remover a categoria. 

# Validar se existe chamado cadastrado antes de consultar ou alterar. 

import random
chamado = {}

while True:
    print("\nSISTEMA DE CHAMADOS DE TI\n")
    print("1 - Criar chamado")
    print("2 - Consultar Chamado")
    print("3 - Alterar Prioridade")
    print("4 - Alterar Status")
    print("5 - Remover Categoria")
    print("6 - Mostrar Chamado Completo")
    print("7 - Encerrar")

    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        chamado["numero"] = input("Digite o numero do chamado: ")
        chamado["solicitante"] = input("Digite o nome do solicitante: ")
        chamado["categoria"] = input("Digite a categoria do chamado: ")
        chamado["prioridade"] = input("Digite a prioridade: ")
        chamado["status"] = "Aberto"

        print("Chamado criado com sucesso!")

        if chamado["prioridade"].lower() == "alta":
            print("Atendimento Urgente!")

    elif opcao == "2":
        if chamado:
            print("\nRESUMO DO CHAMADO")
            print("Chamado número: ", chamado["numero"])
            print("Solicitante do chamado: ", chamado["solicitante"])
            print("Status do chamado: ", chamado["status"])
        else:
            print("Nenhum chamado cadastrado!")

    elif opcao == "3":
        if chamado:
            chamado["prioridade"] = input("Digite a nova prioridade: ")
            print("Prioridade atualizada com sucesso!")
        else:
            print("Nenhum chamado cadastrado!")

    elif opcao == "4":
        if chamado:
            chamado["status"] = input("Digite o novo status: ")
            print("Status atualizado com sucesso!")
        else:
            print("Nenhum chamado cadastrado!")

    elif opcao == "5":
        try:
            del chamado["categoria"]
            print("Categoria removida.")
        except:
            print("Categoria não encontrada!")

    elif opcao == "6":
        if chamado:
            print("\nCHAMADO COMPLETO:")
            for chave, valor in chamado.items():
                print(chave, ":", valor)
        else:
            print("Nenhum chamado cadastrado!")

    elif opcao == "7":
        print("Sistema Encerrado.")
        break

    else:
        print("Opção Invalida")
        

 

 


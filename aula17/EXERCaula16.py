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
    print("sistema de cahmados de TI\n")
    print("1 - Criar chamado")
    print("2 - consultar chamado")
    print("3 - alterar prioridade")
    print("4 - alterar status")
    print("5 - remover categoria")
    print("6 - mostrar chamado completo")
    print("7 - encerrar o chamado")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        chamado["numero"] = random
        chamado["solicitante"] = input("Digite seu nome: ")
        chamado["categoria"] = input("digite a categoria: ")
        chamado["prioridade"] = input("Digite a prioridade: ")
        cahamdo["status"] = "Aberto"

    print("chamado criado com sucesso!")

    if chamado["priorudade"].lower() == "alta":
        print("chamado urgente!")

    elif opcao == "2":
        if chamado:
            print("\nRESUMO DO CHAMADO")
            print("chamado numero: ", chamado["numero"])
            print("solicitante do chamado: ", chamado["solicitante"])
            print("Status do chamado:", chamado["status"])
        else:
            print("Nenhum chamado cadastrado.")


    elif opcao == "3":
        if chamado:


    elif opcao == "4":
        if chamado:

    elif opcao == "5":
        try:
            del chamado["categoria"]
            print("categoria removida.")
        except:

    elif opcao == "6":
        if chamado:
            print("\nCHAMADO COMPLETO:")
            for chave, valor in chamado.items()
                print(chave,",",valor)
        else:
            print("nenhum chamado registrado!")

    elif opcao == "7":
        print("sistema encerrado!")
        break
    else:
        print("Opção invalida.")
        

 

 

# Exercício 4 - Sistema de Cadastro de Projetos 

# Uma empresa deseja criar um sistema simples para cadastrar e acompanhar projetos internos. 

# Cada projeto deve possuir nome, responsável, prazo, orçamento e status. O status inicial de todo projeto deve ser "Em planejamento". 

# O sistema deve permitir cadastrar um projeto, consultar um resumo, atualizar o orçamento, atualizar o status, excluir o prazo, mostrar o projeto completo e encerrar o programa. 

# Além disso, o sistema deve calcular automaticamente a criticidade do projeto com base no orçamento: 

# Se o orçamento for maior que 100000, a criticidade será "Alta". 

# Caso contrário, a criticidade será "Normal". 

# Sempre que o orçamento for atualizado, a criticidade também deve ser recalculada. 

# O sistema deve continuar rodando até o usuário escolher a opção de saída. 

# O programa deve: 

# Criar um dicionário chamado projeto. 

# Criar um menu com while True. 

# Permitir:  

# cadastrar projeto; 

# consultar projeto; 

# atualizar orçamento; 

# atualizar status; 

# excluir prazo; 

# mostrar projeto completo; 

# sair. 

# Definir status inicial como "Em planejamento". 

# Definir criticidade automaticamente com base no orçamento. 

# Recalcular criticidade quando o orçamento for alterado. 

# Usar try/except para tratar orçamento inválido. 

# Usar for e .items() para mostrar o projeto completo. 

# # Validar se há projeto cadastrado antes de consultar ou alterar. 
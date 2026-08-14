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





projeto = {}

while True:
    print("\n ==== Sist PRojeto ====")
    print("1 - Cadastrar Projetos")
    print("2 - consultar projeto")
    print("3 - Atualizar Orçamento")
    print("4 - atualizar status")
    print("5 - excluir prazo")
    print("6 - mostrar projeto completo")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        projeto["nome"] = input("Qaul o nome do projeto: ")
        projeto["responsavel"] = input("Quem é o responsavel? ")
        projeto["prazo"] = input("Digite o prazo para entrega do projeto: ")
        try:
            projeto["orcamento"] = float(input("Digite o orçamento: "))
        except:
            print("orçamento invalido. o orçamento será cadastrado como 0.")
            projeto["orcamento"] = 0

        projeto["status"] = "Em planejamento"

        if projeto["orcamento"] > 100000:
            projeto["criticidade"] = "alta"
        else:
            projeto["criticidade"] = "normal"

        print("Seu projeto foi cadastrado com sucesso.")

    elif opcao == "2":
        if projeto:
            print("\nResumo do projeto:")
            print("Nome do projeto: ", projeto["nome"])
            print("Nome do responsavel: ", projeto["responsavel"])
            print("prazo: ", projeto["prazo"])
            print("orçamento: ", projeto["orcamento"])
            print("criticidade: ", projeto["criticidade"])
            print("status do projeto", projeto["status"])
        else:
            print("Não existe nenhum projeto!")


    elif opcao == "3":
        print("orçamento: ", ["orcamento"])
        if projeto:
            try:
                projeto["orcamento"] = float(input("Digite o orçamento: "))

                if projeto["orcamento"] > 100000:
                    projeto["cristicidade"] = "alta"
                else:
                    projeto["cristicidade"] = "normal"
                print("orçamento atualizado com sucesso!")
                
            except:
                print("orçamento invalido.")

        else:
            print("nenhum projeto cadastrado.")

    elif opcao == "4":
        if projeto:
            print("Status atual: ", ["status"])
            projeto["status"] = input("Digite o novo status do projeto: ")
            print("Status atualizado.")
        else:
            print("nenhum projeto cadastrado.")

    elif opcao == "5":
            try:
                del projeto["prazo"]
                print("prazo excluido.")
            except:
                print("prazo nao encontrado.")

    elif opcao =="6":
        if projeto:
            print("\n Projeto Completo: ")
            for chave, valor in projeto.items():
                print(chave, ":", valor)
        else:
            print("nenhum projeto cadastrado.")

    elif opcao == "7":
        print("Sistema encerrado!")
        break

    else:
        print(" Opção invalida.")

    
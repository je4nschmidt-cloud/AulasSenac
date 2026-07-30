# crie um programa que armazene o dia da semana entre segunda e sexta em uma varivel. o programa deve verificar o valor dessa variavel e imprimir uma mensagem dizendo hoje o é dia da semana se o dia nao for um dia ultil deve imprimir hoje é final de semana.


dia_da_semana = "segunda"  # você pode alterar o valor para testar outros dias da semana

if dia_da_semana == "segunda":
    print("hoje é segunda-feira, dia útil.")
elif dia_da_semana == "terça":
    print("hoje é terça-feira, dia útil.")
elif dia_da_semana == "quarta":
    print("hoje é quarta-feira, dia útil.")
elif dia_da_semana == "quinta":
    print("hoje é quinta-feira, dia útil.")
elif dia_da_semana == "sexta":
    print("hoje é sexta-feira, dia útil.")
else:
    print("hoje é final de semana.")
# import numpy as np

# num = np.array([1,2,3,4,5,6,7,8,9,10])
# print(num)
# print("a media dos numeros é: ", num.mean())
# num_pares = num[num % 2 == 0]
# print("Os numeros pares são: ", num_pares)

# ##alterando o indice.
# num[1] = 0
# num[0:3] = 0


# import numpy as np

# notas = np.array([5.5,8.0,4.0,9.5,6.0,3.5,7.5])
# notas_bonus = notas + 0,5

# print("Notas originais: ", notas)
# print("Novas notas: ", notas_bonus)
# print("Antiga media da turma: ", notas.mean())
# print("Nova media da turma: ", notas_bonus.mean())
# aprovados_nota= nota[nota >= 6]
# print("Notas originais dos aprovados: ", aprovados_nota)
# aprovados_nota_bonus = notas_bonus[notas_bonus >= 6]
# print("Novos aprovados pos bonus: ", aprovados_nota_bonus)
# print("Alunos aprovados com notas originais: ", {len(aprovados_nota)} de {len(notas)})
# print("Alunos aprovados apos nota bonus: ", {len(aprovados_nota_bonus)} de {len(notas_bonus)})


# import numpy as np

# salarios = np.array[ 1.800.0, 2.500.0, 3.200.0, 1.400.0]
# salarios_bonus = salarios * 1.08

# soma_salarios = salarios.sum()
# soma_salarios_bonus = salarios_bonus.sum()

# print(f"Os salarios reajustado sao: {salarios_bonus}")
# print(f"Os salarios antigos somados são: {soma_salarios:.2f}")
# print(f"Os novos salarios somados dão: {soma_salarios_bonus:.2f}")
# print(f"O aumento roral é de: {soma_salarios_bonus:.2f}")


import numpy as np

temp_regis = np.array([2.1,4.5,6.8,8.0,3.2,7.4,1.9,9.1])
temp_exc = temp_regis[temp_regis >= 6]
print("Todas temperaturas: ", temp_regis)
print(f"Temperaturas excedidas: {temp_exc}")
print("Media registrada: ", temp_regis.mean())
print(f"Quantida de alertas: {len(temp_exc)}")




vel_km = np.array([60.0,80.0,100.0,120.0,90.0])
vel_ms = vel_km / 3.6
vel_maior_km = vel_km.max()
vel_menor_ms = vel_ms.min()

print(f"As velocidades em Km/h: {vel_km}")
print(f"As velocidade em M/S: {np.round(vel_ms,2)}")
print("A maior velocidade em metros por segundos: ", {np.round(vel_maior_km,2)})
print("A menor velocidade em metros por segundos: ", {np.round(vel_menor_km,2)})























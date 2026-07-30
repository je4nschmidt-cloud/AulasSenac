

idade = 16
periodo_do_dia =  "tarde"

#if alinhado = if dentro de outro if.

if idade < 18:
   if periodo_do_dia == "manha":
       print("Menor de idade e está na escola pela manhã.")
   elif periodo_do_dia == "tarde":
       print("Menor de idade e está na escola à tarde.")
   else:
       print("Menor de idade e está em casa à noite.")
else:   # Maior de idade.
   if periodo_do_dia == "manha":
       print("Maior de idade e está no trabalho pela manhã.")
   elif periodo_do_dia == "tarde":
       print("Maior de idade e está no trabalho à tarde.")
   else:
       print("Maior de idade e está em casa à noite.")



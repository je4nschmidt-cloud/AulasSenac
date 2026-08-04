planetas = ["Terra", "Marte", "Jupiter", "Saturno","Urano", "Netuno"]

import random

for i in range(3):
    print(random.choice(planetas)) #choice() escolhe um elemento aleatorio da lista



for i in range(1):
    random.shuffle(planetas)
    print(planetas) # shuffle() embaralha a  lista
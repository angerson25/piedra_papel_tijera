#Juego piedra, papel y tijera

import random

#INPUT
c=int(random.uniform(1, 4))


#PROCESAMIENTO

#Asignacion de ataques

print("\n Escoge tu ataque: \n")
# Se despliega el menu
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

j=int(input("Digite su opcion: "))


if (c==1):
    oc = "Piedra"
elif (c==2):
    oc = "Papel"
else :
    oc = "Tijera"

if (j==1):
    oj = "Piedra"
elif (j==2):
    oj = "Papel"
elif (j==3):
    oj = "Tijera"
else: print("ERROR, escogiste una opcion equivocada")

print("--------------------------------------")
print("Tu ataque es: " + str(oj))
print("El ataque de la maquina es: " + str(oc))
print("--------------------------------------")


#Combate

print("--------------------------------------")
if (j==c):
    print("EMPATE")
elif (j==1 and c==3):
    print("GANASTE")
elif (j==2 and c==1):
    print("GANASTE")
elif (j==3 and c==2):
    print("GANASTE")
else: 
    print("PERDISTE")

#FIN


# Realitza un programa en Python que demane una hora per teclat i que mostre el missatge “¡Bon dia!”, “¡Bona vesprada!” o “¡Bona nit!” segons l’hora.
# S’utilitzaran els trams de 6 a 12, de 13 a 20 i de 21 a 5, respectivament.
# NOTA: Sols es tenen en compte les hores, els minuts no s’han d’introduir per teclat.

hora = int(input("Introdueix l'hora (0-23): "))
if 6 <= hora <= 12:
    print("¡Bon dia!")
elif 13 <= hora <= 20:
    print("¡Bona vesprada!")
else:
    print("¡Bona nit!")

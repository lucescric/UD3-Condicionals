# Donats dos nombres sencers, n1 i n2, dissenya un programa en Python que mostre un dels dos missatges:
# “El producte dels dos nombres és positiu o zero”
# o bé,
# “El producte dels dos nombres és negatiu”.
# No has de fer multiplicacio

n1 = int(input("Introdueix el primer nombre: "))
n2 = int(input("Introdueix el segon nombre: "))

if (n1 >= 0 and n2 >= 0) or (n1 < 0 and n2 < 0):
    print("El producte dels dos nombres és positiu o zero")
else:
    print("El producte dels dos nombres és negatiu")

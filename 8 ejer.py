def calcular_tarifa(carnet, practiques):
    # Preus de matrícula per tipus de carnet
    preus_matricula = {"A": 150, "B": 325, "C": 520, "D": 610}

    # Preus per pràctica per tipus de carnet
    preus_practica = {"A": 15, "B": 21, "C": 36, "D": 50}

    carnet = carnet.upper()  # Normalitzem l'entrada

    if carnet not in preus_matricula or carnet not in preus_practica:
        return "Tipus de carnet no vàlid."

    total = preus_matricula[carnet] + practiques * preus_practica[carnet]
    return f"La tarifa total per al carnet {carnet} amb {practiques} pràctiques és de {total}€."


# Exemple d'ús
tipus_carnet = input("Introdueix el tipus de carnet (A, B, C o D): ")
num_practiques = int(input("Introdueix el nombre de pràctiques realitzades: "))

print(calcular_tarifa(tipus_carnet, num_practiques))

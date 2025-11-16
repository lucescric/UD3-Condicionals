# Demanar les dades a l'usuari
hores = float(input("Introduïx el nombre d'hores treballades esta setmana: "))
preu_hora = float(input("Introduïx el preu per hora: "))

# Calcular el salari
if hores <= 40:
    salari = hores * preu_hora
else:
    hores_normals = 40
    hores_extres = hores - 40
    salari = (hores_normals * preu_hora) + (hores_extres * preu_hora * 1.5)

# Mostrar el resultat
print(f"El salari setmanal és: {salari:.2f} €")

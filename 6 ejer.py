# Diccionari amb les assignatures de cada dia
horari = {
    "dilluns": "Matemàtiques",
    "dimarts": "Llengua",
    "dimecres": "Anglès",
    "dijous": "Ciències",
    "divendres": "Educació Física",
}

# Demanar el dia de la setmana
dia = input("Introdueix un dia de la setmana: ").strip().lower()

# Comprovar si el dia és vàlid i mostrar l'assignatura
if dia in horari:
    print(f"A primera hora el {dia} toca {horari[dia]}.")
else:
    print(
        "Dia no vàlid. Intenta-ho amb dilluns, dimarts, dimecres, dijous o divendres."
    )

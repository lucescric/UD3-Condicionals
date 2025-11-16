def calcular_iva(base_imposable, tipus_iva):
    """Calcula la quantitat d'IVA a afegir."""
    if tipus_iva == "general":
        percentatge = 0.21
    elif tipus_iva == "reduït":
        percentatge = 0.10
    elif tipus_iva == "super_reduït":
        percentatge = 0.04
    else:
        # Gestió d'error simple si el tipus no és vàlid
        print("Tipus d'IVA no vàlid. S'aplicarà IVA general (21%) per defecte.")
        percentatge = 0.21
    return base_imposable * percentatge


def aplicar_promocio(preu_amb_iva, codi_promocional):
    """Calcula la quantitat a descomptar segons el codi promocional."""
    if codi_promocional == "nopromo":
        descompte = 0
    elif codi_promocional == "mitat":
        descompte = preu_amb_iva / 2
    elif codi_promocional == "menys5":
        descompte = 5
    elif codi_promocional == "5per":
        descompte = preu_amb_iva * 0.05
    else:
        # Gestió d'error simple si el codi no és vàlid
        print("Codi promocional no vàlid. No s'aplicarà cap promoció per defecte.")
        descompte = 0
    return descompte


def programa_principal():
    # Sol·licitar dades a l'usuari
    try:
        base_imposable = float(input("Introduïx la base imposable (preu sense IVA): "))
        tipus_iva = input(
            "Introduïx el tipus d'IVA (general, reduït, super_reduït): "
        ).lower()
        codi_promocional = input(
            "Introduïx el codi promocional (nopromo, mitat, menys5 o 5per): "
        ).lower()
    except ValueError:
        print(
            "Error: Si us plau, introduïu un valor numèric vàlid per a la base imposable."
        )
        return

    # Calcular l'IVA
    iva_quantitat = calcular_iva(base_imposable, tipus_iva)
    preu_amb_iva = base_imposable + iva_quantitat

    # Calcular el descompte
    descompte_quantitat = aplicar_promocio(preu_amb_iva, codi_promocional)
    preu_final = preu_amb_iva - descompte_quantitat

    # Mostrar resultats amb format
    print("\n--- Resultat ---")
    print(f"Base imposable:           {base_imposable:8.2f}€")
    print(f"IVA ({tipus_iva}):          {iva_quantitat:8.2f}€")
    print(f"Preu amb IVA:             {preu_amb_iva:8.2f}€")
    print(f"Codi promocional ({codi_promocional}): {descompte_quantitat * -1:8.2f}€")
    print(f"El preu final és:         {preu_final:8.2f}€")


# Executar el programa
if __name__ == "__main__":
    programa_principal()

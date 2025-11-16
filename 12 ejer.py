def calculadora_bandera():
    print("Calculadora de preus - BanderesDelMon.es")

    # Entrada de dades
    alt_cm = int(input("Introduïx l’altura de la bandera en cm: "))
    ample_cm = int(input("Introduïx l’ample de la bandera en cm: "))
    escut_input = input("¿Vols escut bordat? (s/n): ").strip().lower()

    # Càlculs
    superficie = alt_cm * ample_cm
    preu_base = superficie * 0.01
    escut = 2.50 if escut_input == "s" else 0.00
    enviament = 3.25
    total = preu_base + escut + enviament

    # Sortida
    print("\nGràcies. Ací té el detall de la seua compra:")
    print(f"Bandera de {superficie} cm²: {preu_base:.2f} €")
    print(f"{'Amb escut' if escut_input == 's' else 'Sense escut'}: {escut:.2f} €")
    print(f"Gastos d’enviament: {enviament:.2f} €")
    print(f"Total: {total:.2f} €")


# Executar la calculadora
calculadora_bandera()

# Sol·licitem les coordenades del punt
x = float(input("Introdueix la coordenada x: "))
y = float(input("Introdueix la coordenada y: "))

# Determinem la posició del punt
if x > 0 and y > 0:
    print("El punt està situat en el primer quadrant.")
elif x < 0 and y > 0:
    print("El punt està situat en el segon quadrant.")
elif x < 0 and y < 0:
    print("El punt està situat en el tercer quadrant.")
elif x > 0 and y < 0:
    print("El punt està situat en el quart quadrant.")
elif x != 0 and y == 0:
    print("El punt està situat en l’eix d’abscisses.")
elif x == 0 and y != 0:
    print("El punt està situat en l’eix d’ordenades.")
elif x == 0 and y == 0:
    print("El punt està situat en l’origen de coordenades.")
else:
    print("Coordenades no reconegudes.")

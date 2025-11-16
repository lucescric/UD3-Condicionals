print("Este programa resol equacions de primer grau del tipus ax + b = 0")

# Sol·licitem els valors de a i b
a = float(input("Per favor, introduïsca el valor de a: "))
b = float(input("Per favor, introduïsca el valor de b: "))

# Comprovem si l'equació té solució
if a == 0:
    if b == 0:
        print("L'equació té infinites solucions.")
    else:
        print("Esta equació no té solució.")
else:
    x = -b / a
    print(f"x = {x}")

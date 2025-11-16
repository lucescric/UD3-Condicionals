# Bloque 1
if x >= 0:
    x += 1
elif x >= 1:
    x = x + 2

# x inicial = 0
# La condición if x >= 0: es Verdadera (ya que 0≥0)
# se ejecuta x +=1 en esta instrucción pasamos x a valer 1
# La condición elif x >= 1: no se evalúa porque la primera condición ya fue Verdadera
# El valor final de X es 1

# Bloque 2

if x >= 0:
    x += 1

if x >= 1:
    x = x + 2

# x inicial = 0
# La condición if x >= 0: es Verdadera (ya que 0≥0)
# se ejecuta x +=1 en esta instrucción pasamos x a valer 1
# Luego se evalúa la segunda condición if x >= 1: que también es Verdadera (ya que 1≥1)
# se ejecuta x = x + 2 en esta instrucción pasamos x a valer 3
# El valor final de X es 3


# Bloque 3
if x < 0:
    x = x + 2
else:
    x += 1
x -= 1

# x inicial = 0
# La condición if x < 0: es Falsa (ya que 0<0)
# Por lo tanto se ejecuta el bloque else: que contiene x += 1
# En esta instrucción pasamos x a valer 1
# Luego se ejecuta la instrucción x -= 1 que está fuera del bloque condicional
# En esta instrucción pasamos x a valer 0
# El valor final de X es 0


# Bloque 4
if x > 0:
    if x <= 1:
        x += 1
    else:
        x -= 1

# x inicial = 0
# La condición if x > 0: es Falsa (ya que 0>0)
# Por lo tanto no se ejecuta ningún bloque condicional
# El valor final de X es 0

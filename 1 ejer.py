consum = 0.0
velocitat = 120
if velocitat > 80:
    consum = 15.00
elif velocitat > 100:
    consum = 12.00
elif velocitat > 120:
    consum = 10.00

print(consum)


# La primera condició  és cert (120 > 80), per tant s'executa .
# Els següents blocs  no s'executen, perquè en una estructura if–elif–else, només s'executa el primer bloc que compleix la condició.
# Encara que  també és cert, aquest bloc s'ignora perquè el primer  ja s'ha executat.

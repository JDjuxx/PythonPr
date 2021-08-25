# Función que recepta varios valores y los multiplica entre sí

def multiplicacionDeValores(*valores):
    totalMultiplicacion = 1
    for valor in valores:
        totalMultiplicacion *= valor
    return totalMultiplicacion
print(f'La Multiplicación total es {multiplicacionDeValores
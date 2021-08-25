# Función recursiva que devuelve la serie inversa del número dado

def funcionRecursiva(numero):
    if numero == 1:
        return 1
    elif numero > 1:
        print(f'Numero: {numero}')
        return funcionRecursiva(numero-1)

print(f'Numero: {funcionRecursiva(7)}')
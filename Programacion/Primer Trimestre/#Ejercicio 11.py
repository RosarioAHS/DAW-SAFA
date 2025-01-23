#Ejercicio 11
def palabra_mas_larga(lista_palabras):
    # Uso la función max() con la clave de longitud key para encontrar la palabra más larga
    return max(lista_palabras, key=len)

# Ejemplo de uso:
palabras = ["manzana", "banana", "kiwi", "cereza", "fresa"]
resultado = palabra_mas_larga(palabras)
print("La palabra más larga es:", resultado)

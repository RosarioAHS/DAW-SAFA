def reemplazar_letras(cadena, letra_original, letra_nueva):
    # Uso el método replace para sustituir las ocurrencias de letra_original por letra_nueva
    nueva_cadena = cadena.replace(letra_original, letra_nueva)
    return nueva_cadena

texto = "Hola Mundo"
letra_a_reemplazar = input("Ingresa la letra a reemplazar: ")  # Letra a reemplazar
letra_de_reemplazo = input("Ingresa la letra nueva: ")  # Letra con la que reemplazar

#Mostramos el resultado
resultado = reemplazar_letras(texto, letra_a_reemplazar, letra_de_reemplazo)
print("Cadena modificada:", resultado)

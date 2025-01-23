#Ejercicio 5

def eliminar_espacios(cadena):
    return cadena.replace( " ","")

texto = "Hola Jamon"
texto_sin_espacios = eliminar_espacios(texto)
print(texto_sin_espacios)
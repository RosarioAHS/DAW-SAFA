#Ejercicio 6

def eliminar_vocales(cadena):

    cadena = cadena.replace("a", "")  #Uso el metodo de replace como el ej 5
    cadena = cadena.replace("e", "")
    cadena = cadena.replace("i", "")
    cadena = cadena.replace("o", "")
    cadena = cadena.replace("u", "")
    cadena = cadena.replace("A", "")
    cadena = cadena.replace("E", "")
    cadena = cadena.replace("I", "")
    cadena = cadena.replace("O", "")
    cadena = cadena.replace("U", "")
    return cadena

texto = "Hola Jamon"
texto_sin_vocales = eliminar_vocales(texto)
print(texto_sin_vocales)

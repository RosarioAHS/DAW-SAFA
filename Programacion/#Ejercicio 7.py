#Ejercicio 7

def contar_palabras(cadena):
    palabras = cadena.split() #Utilizo el split para eliminar los espacios en blancos asi no me los cuenta y tmb para contar solo las PALABRAS
    return len(palabras)

# Ejemplo de uso
texto = "Hola Mundo, ¿cómo estás?"
numero_de_palabras = contar_palabras(texto)
print(f"El número de palabras es: {numero_de_palabras}")

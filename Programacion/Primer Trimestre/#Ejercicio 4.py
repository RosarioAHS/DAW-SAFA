#Ejercicio 4

def invertir_texto(texto):

    return texto[::-1] #el :: indica que selecciono toda la fila, el -1 para que recorra la fila de izq a der osea al reves.

texto = "Jamon"
texto_invertido = invertir_texto(texto)
print(texto_invertido)
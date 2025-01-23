#Ejercicio 8

def es_palindromo(cadena):
    # Elimino los espacios en blanco y convierto todo a minúsculas
    cadena_limpia = "".join(cadena.split()).lower()
    
    # Compruebo si la cadena limpia es igual a su reverso.
    return cadena_limpia == cadena_limpia[::-1]

texto = "A man a plan a canal Panama" #Busque una palabra que se pueda leer igual al reves
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

def calcular_media_y_clasificacion(notas):
    """Calcula la media de una lista de notas y devuelve la clasificación correspondiente."""
    if not notas:  # Verificamos que la lista no esté vacía
        return "La lista de notas está vacía."

    # Calcular la media
    media = sum(notas) / len(notas)

    # Clasificación según la media
    if media < 5:
        clasificacion = "Suspenso"
    elif 5 <= media < 7:
        clasificacion = "Aprobado"
    elif 7 <= media < 9:
        clasificacion = "Notable"
    else:
        clasificacion = "Sobresaliente"

    return f"La media calculada es: {media:.2f}. Clasificación: {clasificacion}"

# Ejemplo de uso
notas = [5.6, 7, 6.2, 8]
resultado = calcular_media_y_clasificacion(notas)
print(resultado)

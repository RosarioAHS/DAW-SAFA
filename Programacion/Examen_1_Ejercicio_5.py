def es_contrasena_segura(contrasena):
    """
    Verifica si una contraseña es segura según las condiciones:
    - Empieza y termina con una letra mayúscula.
    - Contiene al menos un número.
    - Contiene al menos uno de los siguientes símbolos: ., _, #.
    """
    if not contrasena:
        return False  # Si la cadena está vacía, no es segura

    # Condición 1: Empieza y termina por una letra mayúscula
    if not (contrasena[0].isupper() and contrasena[-1].isupper()):
        return False

    # Condición 2: Contiene algún valor numérico
    if not any(char.isdigit() for char in contrasena):
        return False

    # Condición 3: Contiene uno de los símbolos especificados
    if not any(char in "._#" for char in contrasena):
        return False

    # Si todas las condiciones se cumplen
    return True

# Ejemplo de uso
contrasena = "A123_bC"
resultado = es_contrasena_segura(contrasena)
print(f"¿Es la contraseña '{contrasena}' segura? {resultado}")

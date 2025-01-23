def contar_signos_puntuacion(texto):
    # Definimos los signos de puntuación que queremos contar
    signos = {
        "comas": ",",
        "puntos": ".",
        "interrogaciones": "?",
        "dos_puntos": ":",
        "punto_y_coma": ";",
        "paréntesis": "()",
        "corchetes": "[]",
        "comillas": "\"",
        "admiración": "!",
        "diéresis": "ü",
        "guión": "-"
    }
    
    # Diccionario para almacenar los conteos
    conteos = {nombre: 0 for nombre in signos}
    
    # Recorremos el texto para contar cada signo
    for char in texto:
        for nombre, simbolo in signos.items():
            if char in simbolo:
                conteos[nombre] += 1
    
    # Mostramos los resultados
    print("Signos de puntuación encontrados:")
    for nombre, cantidad in conteos.items():
        if cantidad > 0:  # Mostramos solo los signos que están presentes
            print(f"Número de {nombre} : {cantidad}")

texto = """En las ciudades de Piltover y Zaun, se palpa el desasosiego en el ambiente: inventores, ladrones, 
políticos y señores del crimen buscan liberarse de las ataduras de una sociedad fragmentada. 
Mientras la rebelión va cobrando fuerza, dos hermanas roban un artefacto de poder inimaginable. 
Los descubrimientos y el peligro son el trasfondo sobre el que nacerán héroes y se romperán vínculos. 
¿Servirá este poder para cambiar el mundo o lo llevará a la ruina? Este es el mundo de Arcane."""

contar_signos_puntuacion(texto)

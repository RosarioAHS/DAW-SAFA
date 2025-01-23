def ahorcado(palabra):
    palabra = palabra.lower()
    vidas = 5
    letras_citadas = set()  # Usamos un conjunto para evitar duplicados
    progreso = ["_" for _ in palabra]

    print("¡Bienvenido al juego del Ahorcado!")
    
    while vidas > 0:
        print("\n" + "-" * 50)
        print(f"Vidas: {vidas}")
        print(f"Letras citadas: {', '.join(sorted(letras_citadas))}")
        print(f"Palabra: {' '.join(progreso)}")
        
        letra = input("Dime una letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Introduce solo una letra.")
            continue

        if letra in letras_citadas:
            print("Ya dijiste esa letra. Intenta con otra.")
            continue
        
        letras_citadas.add(letra)

        if letra in palabra:
            print("¡Has acertado!")
            for i, l in enumerate(palabra):
                if l == letra:
                    progreso[i] = letra
        else:
            print("Letra incorrecta.")
            vidas -= 1

        if "_" not in progreso:
            print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
            break
    
    if vidas == 0:
        print(f"\nHas perdido. La palabra era: {palabra}")

# Ejemplo de uso
ahorcado("patinete")

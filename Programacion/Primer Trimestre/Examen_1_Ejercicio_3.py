def alumnos_dominio_centro(lista_alumnos, dominio_centro="safareyes.es"):
    #Devuelve una lista de alumnos cuyo email pertenece al dominio del centro
    return [alumno for alumno in lista_alumnos if alumno['email'].split('@')[1] == dominio_centro]

def alumno_primer_apellido(lista_alumnos):
    #Devuelve al primer alumno en orden alfabético por el primer apellido
    return min(lista_alumnos, key=lambda alumno: alumno['apellidos'].split(',')[0].strip())

def alumno_primera_letra_dni(lista_alumnos):
    #Devuelve al primer alumno en orden alfabético por la letra del DNI
    return min(lista_alumnos, key=lambda alumno: alumno['dni'][-1])

# List
alumnos = [
    {
        "nombre": "Enrique",
        "apellidos": "García, Migueza",
        "dni": "12345678K",
        "email": "egarciamigueza@safareyes.es"
    },
    {
        "nombre": "Paloma",
        "apellidos": "Machado, López",
        "dni": "12345678Z",
        "email": "pmachadolopez@hotmail.es"
    },
    {
        "nombre": "Antonio",
        "apellidos": "Romero, Domínguez",
        "dni": "12345678A",
        "email": "aromerodominguez@safareyes.es"
    }
]

# a) Alumnos con email del dominio "safareyes.es"
alumnos_centro = alumnos_dominio_centro(alumnos)
print("Alumnos del dominio safareyes.es:")
print(alumnos_centro)

# b) Primer alumno según el orden del primer apellido
primer_alumno_apellido = alumno_primer_apellido(alumnos)
print("\nPrimer alumno por orden del primer apellido:")
print(primer_alumno_apellido)

# c) Primer alumno según la letra del DNI
primer_alumno_dni = alumno_primera_letra_dni(alumnos)
print("\nPrimer alumno por orden de la letra del DNI:")
print(primer_alumno_dni)

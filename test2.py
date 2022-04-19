materia = []
while len(materia) < 8:
    materias = input("Ingrese una materia en curso: ")
    materia.append(materias)
    while len(materia)>4:
        respuesta = input("Quiere ingresar otra materia? SI o NO")
        if respuesta.lower == ("si"):
            materias = input("Ingrese una materia en curso: ")
            materia.append(materias)
        else: print("prosedamos a cargar las notas")

materias = ["lengua","matematica","fisica","geografia"]
materiasNotas = {} 

def promedioEvaluacion(materias):
    for materia in materias:
        nota = input("Ingrese la nota de " + materia + ": " )
        materiasNotas[materia] = nota
    
    promedio = 0
    for materia in materias:
        promedio = promedio + float(materiasNotas[materia])
        if promLengua < 8 and promLengua >= 6:
            print("Lengua: materia aprobada")
        elif promLengua < 6:
            print("Lengua no esta aprobada")


    promedio = promedio / len(materias)
    print(round(promedio, 2))
    
promedioEvaluacion(materias)



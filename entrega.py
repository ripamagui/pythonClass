#Realizar los siguientes ejercicios: 
#1. Desarrollar un programa que le pida al alumno todas las materias que está cursando (al menos  4) y luego se le debe pedir las respectivas notas de los 3 parciales de las asignaturas  ingresadas. Por último el programa debe calcular el promedio de las evaluaciones y definir por  cada una de ellas: 
#∙ Si la materia tiene como promedio un 8 o más: Materia promocionada. 
#∙ Si la materia tiene como promedio una nota menor a 8 pero mayor o igual a 6: Materia  aprobada. 
#∙ Si la materia tiene como promedio una nota menor que 6: Materia desaprobada. 


materia = []
while len(materia) < 8:
    materias = input("Ingrese una materia en curso: ")
    materia.append(materias)
    while len(materia)>4:
        respuesta = input("Quiere ingresar otra materia? SI o NO")
        if respuesta == respuesta.lower("si"):
            materias = input("Ingrese una materia en curso: ")
            materia.append(materias)
        else: print("prosedamos a cargar las notas")


materias = input("Ingrese una materia en curso: ")
materia.append(materias)
print(materia)

notas = []
def nota():
    calificacion = float(input(f"Ingrese primer nota de la materia {materia(1)}: "))
    notas.append (calificacion)
    promNotas = notas / len(notas)
    if promNotas >= 8:
        print ("Materia promosionada")
    elif 8>promNotas>=6:
        print(f"Materia Aprobada. Debe rendir final de {materia(1)}")

nota()


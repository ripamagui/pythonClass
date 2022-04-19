

#Lengua, matemática, física
#Definir las variables
lengua = "lengua"
matematica = "matemática"
fisica = "física"
materiaError = "Esta materia no pertenece al plan del alumno"

#Elegir las materias para cargar datos:
materiaOriginal = input("Qué materia estas evaluando?: ")
materia= materiaOriginal.lower()
if materia == lengua:
    promLengua=float(input("Ingrese el promedio de lengua para el alumno: "))
elif materia == matematica:
    promMatematica=float(input("Ingrese el promedio de matematica para el alumno: "))
elif materia == fisica:
    promFisica=float(input("Ingrese el promedio de fisica para el alumno: "))
else: print(materiaError)

materia2Original = input ("Ingrese otro materia: ")
materia2= materia2Original.lower()
if materia2 == lengua:
    promLengua=float(input("Ingrese el promedio de lengua para el alumno: "))
elif materia2 == matematica:
    promMatematica=float (input("Ingrese el promedio de matemática para el alumno: "))
elif materia2 == fisica:
    promFisica=float (input("Ingrese el promedio de física para el alumno: "))
else: print((materiaError))

materia3Original = input ("Ingrese otro materia: ")
materia3= materia3Original.lower()
if materia3 == lengua:
    promLengua=float(input("Ingrese el promedio de lengua para el alumno: "))
elif materia3 == matematica:
    promMatematica=float(input("Ingrese el promedio de matemática para el alumno: "))
elif materia3 == fisica:
    promFisica=float(input("Ingrese el promedio de física para el alumno: "))
else: print(materiaError)


#Calcular el promedio de estas materias
promGeneral= (promLengua + promMatematica + promFisica)/3
print("Promedio del alumno ", promGeneral)


#Si las materias tienen menor 8 pero mayor igual a 6 aprueba
#Si las materias tienen menor que 6 desaprueban

if promLengua < 8 and promLengua >= 6:
    print("Lengua: materia aprobada")
elif promLengua < 6:
    print("Lengua no esta aprobada")

if promMatematica < 8 and promMatematica >= 6:
    print("Matemática: materia aprobada")
elif promMatematica < 6: 
    print("Matemática no esta aprobada")

if promFisica < 8 and promFisica >= 6:
    print("Física: materia aprobada")
elif promFisica <6: 
    print("Física no esta aprobada")

#Si las 3 materias están aprobadas aprueban la cursada
if promLengua >= 6 and promMatematica >=6 and promFisica >=6:
    print("El alumno aprobo la cursada") 
else: print("El alumno no aprueba la cursada") #No hay condicion para 2 materias aprobadas, por eso soluciono asi en vez de hacer todas las convinaciones posibles. 

#Si las materias tienes mayor promedio que 8 promociona
#Si una de las materias está aprobada pero no promociona va a rendir final
if promGeneral >= 8:
    print("El alumno promociona")
if promLengua < 8 and promLengua >= 6:
    print("Lengua a final")
if promMatematica < 8 and promMatematica >= 6:
    print("Matematica a final")
if promFisica < 8 and promFisica >= 6:
    print("Física a final")






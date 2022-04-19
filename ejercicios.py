#Funsiones
#voy a definir una funsion con def el nombre de la funsion () 
def funsion1():
    print("Esto es una funsion")

funsion1() #Asi llamo a la funsion 

#cuando defino una funsion puedo ponerle parametros dentro de los () 
#este valor lo voy a definir dentro de los () cuando la llame 
#el parametro es lo que cambia en la funsion de toda la logica que tiene 

def conversacion(mensaje):
    print("hola como estas?")
    print(mensaje)
    print("Adios")


opciones=int(input("Elije una opcion (1, 2, 3): "))
if opciones ==1:
    conversacion("Elegiste la opcion 1")
elif opciones ==2:
    conversacion("Elegiste la opcion 2:")
elif opciones ==3: 
    conversacion("Elegiste la opcion 3")
else:
    print ("Elige una opcion valida")

def suma(a,b):
    print(f"Se suman dos numeros {a} y {b}")
    resultado = a+ b
    return resultado #si no le pongo esto no me va a devolver el resultado de la suma y ademas asi la puedo almacenar
    #return me regresa un valor en una funsion
sumatoria = suma(1,4)
print(sumatoria)

#si una variable la defino en mayusculas pasa a ser una constante 
# numero**numero me da el primero elevado al segundo. Los** eleva
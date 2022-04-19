from importlib.util import MAGIC_NUMBER
from itertools import count
from unicodedata import name


print ("hola mundo") #todo lo que es texto va a ir entre ""
print ("Hola Clase ") 
print ("Esto esta funcionando bien") 
print ("vamos a compilar varias frases seguidas y cuentas", 20+30, "esta cuenta funciona si da 50")
#variables
a = 20+30
c = "cristian es el profesor"
c_a = "cristian y alexis son los profesores" #las variables deben ser palabras unidas o unidas por _
print(a,c)
print("ejemplo")
numero = 2
Numero ="dos"
print(type(numero),numero)
print(type(Numero),Numero)
# += es para adicionar informacion a una variable ya definida 
nom = "Pepe"
nom += " "
nom += "Argento"
print(nom)
#Metodos: instruccion para hacer algo sin volver a escribir el codigo 
nombre = "Pepe"
print(nombre.upper())
print(nombre.count("e")) #ojo porq ve si son mayusculas o minisculas. Suele usarse como prueba logica para saber que hay un correo con el @
print(nombre.replace("e","i"))
print(nombre.strip()) #elimina espacios blancos al principio o al final de la variable 

name = input("Ingrese su nombre: ") #input se usa para solicitar informacion y guardar en una variable
name += " "
name += input("Ingrese su apellido: ")
print("hello " + name)
#el input el unico dato que obtiene es un string por eso para "sumarlo" debemos convertir el dato
#int para que sea un numero entero 
#float para un numero decimal 
#para ser a la inversa o sea volverlo string vamos a poner str()
nombre=input("ingrese nombre: ")
nombre+=input("ingrese apellido: ")
edad=int(input("ingrese edad: "))
altura=float(input("ingrese altura: "))
ahorros=float(input("ingrese sus ahorros: "))
sueldo= float(input("ingrese su sueldo: "))
saldo=float (ahorros+sueldo)
print( f" hola {nombre}  tienes {edad} años , su altura  es de {altura} metros. Su ahorro total es de {ahorros} pesos , con sueldo neto total de {sueldo} y un saldo de {saldo}")
#la f permite que se interprete lo que esta entre {} como variables 
# el \n te permite hacer salto de linea pero deben estar dentro del "" del texto

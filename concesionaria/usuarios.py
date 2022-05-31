from tokenize import Name
from unicodedata import name


class Invitado:
    def __init__(self, nombre, passw, telefono, categoria ='Invitado'):
        self.nombre = nombre
        self.categoria = categoria 
        self.passw = passw
        self.telefono = telefono

class Empleado:
    def __init__(self, nombre, passw, numEmpleado, categoria='Empleado'):
        self.nombre = nombre
        self.passw = passw
        self.numEmpleado = numEmpleado
        self.categoria = categoria

userData = {
    "nombre" : ["Tigri" , "Facu" , "Magui"], 
    "usuario" : ["tgr", "fml", "mar"],
    "contraseña" : ["123", "345", "tito1"],
    "permiso" : ["Admin", "Visita", "Empleado"] 
    }

def crearUsuario():
    nombrePropio= input("Ingrese su nombre: ")
    usuarioNuevo = input("Ingrese un usuario de 3 letras: ")
    usuarioNuevo= usuarioNuevo.lower()
    passw1, passw2 = pedirPassw()
    while passw1 != passw2:
        passw1, passw2 = pedirPassw()

    if passw1 == passw2:
        userData["contraseña"].append(passw1)
        userData["nombre"].append(nombrePropio)
        userData["usuario"].append(usuarioNuevo)
        nuevaVisita = "Visita"
        userData["permiso"].append(nuevaVisita)



def pedirPassw():
    passw1 = input("Defina una contraseña: ")
    passw2 =input("Vuelva a ingresar su contraseña: ")
    return passw1, passw2



autos =  {
    "marca": ["Ford" , "Volvo" , "Mercedez"],
    "color": ["Naranja" , "Azul" , "Gris"], 
    "motor" : ["V8", "V6 Plus", "V10"],
    "precio" : [10000, 30000, 2343],
    "pasajeros" : [20, 23, 40] ,
    "km": [12345, 22334, 90899]
    }
#['Falcon','Tunus','Focus']

bondis = {
    "marca": ["Ford" , "Volvo" , "Mercedez"],
    "color": ["Naranja" , "Azul" , "Gris"], 
    "motor" : ["V8", "V6 Plus", "V10"],
    "precio" : [10000, 30000, 2343],
    "pasajeros" : [20, 23, 40] ,
    "km": [12345, 22334, 90899]
    }

colectivoStore = []
autoStore = []
motoStore = []
biciStore = []
camionStore = []
acopladoStore = []
camionetaStore = []
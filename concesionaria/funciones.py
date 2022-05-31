
from acoplados import Acoplado
from usuarios import userData, bondis, autos, colectivoStore, autoStore , motoStore , biciStore, camionetaStore, camionStore, acopladoStore
from colectivo import Colectivo
from autos import Auto
from motos import Moto
from bici import  Bicicleta
from camioneta import Camioneta
from camiones import Camiones




#Logeo e inicio del programa

def login():
    userName = input("Usuario: ")
    passw = input ('Password: ')
    logueado = False
    usuariologueado = {}
    for user in userData["usuario"]:
        if userName == user:
            indexUser = userData["usuario"].index(user)
            if passw == userData["contraseña"][indexUser]:
                nivelPermiso = userData["permiso"][indexUser]
                usuariologueado = {'nombre' : userData["nombre"][indexUser], 'usuario' : userData["usuario"][indexUser], 'permiso' : nivelPermiso}
                logueado = True
    if logueado == True:
        return logueado, usuariologueado
    else:
        return logueado, usuariologueado  

#Crear la base
def baseVehiculos():
    baseAuto()
    baseMoto()
    baseBici()
    baseColectivo()
    baseCamion()
    baseCamioneta()
    baseAcoplado()


#Menu de inicio segun permisos

def menuWelcome(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado):
    if usuariologueado['permiso'] == "Visita":
        print("\n  Ustede es Visita  \n ")
        menuOpciones (usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
    elif usuariologueado['permiso'] == 'Admin':
        print("\n  Ustede es Administrador  \n ")
        menuOpciones (usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
    elif usuariologueado['permiso'] == 'Empleado':
        print("\n  Ustede es Empleado  \n ")
        menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)


#Menu de opciones que puede hacer el ususario

def menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado):
    try:
        ops = int(input("\n Ingrese la accion de que desea: \n 1. Ver Vehiculos \n 2. Modificar vehiculos \n 3. Crear Vehiculo \n 4. Modificar ususarios \n 5. Salir \n"))
        if ops == 1:
            vistaProductos(usuariologueado, autoStore, motoStore, biciStore, colectivoStore, camionStore, acopladoStore, camionetaStore)
        elif ops == 2 and usuariologueado["permiso"] != "Visita":
            editarProductos(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore, camionStore, acopladoStore, camionetaStore, logueado)
        elif ops == 3 and usuariologueado["permiso"] == "Admin": 
            crearProductos(usuariologueado)
        elif ops == 4 and usuariologueado["permiso"] == "Admin":
            modificarUsuario(userData)
        elif ops == 5: 
            print("\nCERRO SESION \n Gracias por su visita")
            return logueado == False
        else:
            print("No tiene permisos para esta acción.\n")
        menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
    except:print("\nNo es una opcione correcta.\n")


#Menu para VER

def vistaProductos(usuariologueado, autoStore, motoStore, biciStore, colectivoStore, camionStore, acopladoStore, camionetaStore):
    try:
        print("\n VISUALIZACION DE PRODUCTOS \n")
        categoriaProducto = int(input('MENU DE PRODUCTOS: \n 1. Autos \n 2. Motos \n 3. Bicicletas \n 4. Camionetas \n 5. Colectivos \n 6. Camiones \n 7.Acoplados \n \n INGRESE EL NUMERO DE LA OPCION DESEADA   '))
        if categoriaProducto == 1:
            mostrarAuto(usuariologueado , autoStore)
        if categoriaProducto == 2:
            mostrarMoto(usuariologueado , motoStore)
        if categoriaProducto == 3:
            mostrarBici(usuariologueado , biciStore)
        if categoriaProducto == 4:
            mostrarCamioneta(usuariologueado, camionetaStore)
        if categoriaProducto == 5:
            mostrarColectivo(usuariologueado , colectivoStore)
        if categoriaProducto == 6:
            mostrarCamion(usuariologueado, camionStore)
        if categoriaProducto == 7:
            mostrarAcoplado(usuariologueado, acopladoStore)
    except:
        print('Esto no es una opcion correcta.')

#Menu para EDITAR 

def editarProductos(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore, camionStore, acopladoStore, camionetaStore, logueado):
        print("\n EDITAR PRODUCTOS \n")
        opcEditar = int(input("\n MENU EDICION: \n 1. Precio \n 2. KM \n 3. Otros datos\n 4. Volver al menu pricipal\n "))
        if opcEditar == 1 and usuariologueado["permiso"] == "Admin":
            categoriaProducto = int(input('\nEDICION PRECIOS\n MENU DE PRODUCTOS: \n 1. Autos \n 2. Motos \n 3. Bicicletas \n 4. Camionetas \n 5. Colectivos \n 6. Camiones \n 7.Acoplados \n \n INGRESE EL NUMERO DE LA OPCION DESEADA   \n'))
            if categoriaProducto == 1:
                print(f"Autos en el consecionario: ")
                mostrarAuto(usuariologueado, autoStore)
                autoModif = int(input("Que nùmero de auto desea modificar?: "))
                nuevoPrecio =  int(input("Cual es el nuevo precio?: "))
                autoStore[autoModif].cambiarPrecio(nuevoPrecio)
                print(f"El auto quedo modificado con los siguientes datos: ", autoStore[autoModif].adminMostrar())
            elif categoriaProducto == 2:
                print(f"Motos en el consecionario: ")
                mostrarMoto(usuariologueado, motoStore)
                motoModif = int(input("Que número de moto desea modificar?: "))
                nuevoPrecio =  int(input("Cual es el nuevo precio?: "))
                motoStore[motoModif].cambiarPrecio(nuevoPrecio)
                print(f"La moto que modifico quedo con los siguientes datos: ", motoStore[motoModif].adminMostrar())
            elif categoriaProducto == 3:
                print(f"Bicicletas en el consecionario: ")
                mostrarBici(usuariologueado, biciStore)
                biciModif = int(input("Que número de bicicleta desea modificar?: "))
                nuevoPrecio =  int(input("Cual es el nuevo precio?: "))
                biciStore[biciModif].cambiarPrecio(nuevoPrecio)
                print(f"La bicicleta que modifico quedo con los siguientes datos: ", biciStore[biciModif].adminMostrar())
            elif categoriaProducto == 4:
                print(f"Camionetas en el consecionario: ")
                mostrarCamioneta(usuariologueado, camionetaStore)
                chataModif = int(input("Que número de camioneta quiere modificar? "))
                nuevoPrecio = int(input("Cual es el nuevo precio?: "))
                camionetaStore[chataModif].cambiarPrecio(nuevoPrecio)
                print(f"La camioneta quedo modificada con los siguientes datos: ", camionetaStore[chataModif].adminMostrar())
            elif categoriaProducto == 5:
                print(f"Colectivos en el concecionario: ")
                mostrarColectivo(usuariologueado, colectivoStore)
                coleModif = int(input("Que nùmero de colectivo desea modificar?: "))
                nuevoPrecio = int(input("Cual es el nuevo precio?: "))
                colectivoStore[coleModif].cambiarPrecio(nuevoPrecio)
                print(f"El colectivo quedo modificado con los siguientes datos: ", colectivoStore[coleModif].adminMostrar())
            elif categoriaProducto == 6:
                print(f"Camiones en el concecionario: ")
                mostrarCamion(usuariologueado, camionStore)
                mioncaModif = int (input(" Que nùmero de camion quiere modificar?: "))
                nuevoPrecio = int (input("Cual es el nuevo precio?: "))
                camionStore[mioncaModif].cambiarPrecio(nuevoPrecio)
                print(f"El camion que modificó quedo con los siguientes datos: ", camionStore[mioncaModif].adminMostrar())
                #El camion debe poder cambiar ademas si tiene acopado 
            elif categoriaProducto == 7:
                print(f"Acoplados en el concecionario: ")
                mostrarAcoplado(usuariologueado, acopladoStore)
                acopladoModif = int (input("Que número de acoplado desea modificar?: "))
                nuevoPrecio = int(input("Cual es el nuevo precio?: "))
                acopladoStore[acopladoModif].cambiarPrecio(nuevoPrecio)
                print(f"El acoplado quedo moficado con los siguientes datos: ", acopladoStore[acopladoModif].adminMostrar())
                #El acoplado debe poder cambiar si va con camion o no
            else: 
                print("No es una opcion correcta, intente nuevamente")
                menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
        elif opcEditar == 2:
            categoriaProducto = int(input('\n EDICION KM\n MENU DE PRODUCTOS: \n 1. Autos \n 2. Motos \n 3. Bicicletas \n 4. Camionetas \n 5. Colectivos \n 6. Camiones \n 7.Acoplados \n \n INGRESE EL NUMERO DE LA OPCION DESEADA   \n'))
            if categoriaProducto == 1:
                print(f"Autos en el consecionario: ")
                mostrarAuto(usuariologueado, autoStore)
                autoModif = int(input("Que nùmero de auto desea modificar?: "))
                nuevosKm =  int(input("Cuantos Km tiene el vehiculo?: "))
                autoStore[autoModif].cambiarKM(nuevosKm)
                print(f"El auto quedo modificado con los siguientes datos: ", autoStore[autoModif].mostrar())
            elif categoriaProducto == 2:
                print(f"Motos en el consecionario: ")
                mostrarMoto(usuariologueado, motoStore)
                motoModif = int(input("Que número de moto desea modificar?: "))
                nuevosKm =  int(input("Cuantos Km tiene el vehiculo?: "))
                motoStore[motoModif].cambiarKM(nuevosKm)
                print(f"La moto que modifico quedo con los siguientes datos: ", motoStore[motoModif].mostrar())
            elif categoriaProducto == 3:
                print("La bici no cuenta KM, no podra modificar nada")
            elif categoriaProducto == 4:
                print(f"Camionetas en el consecionario: ")
                mostrarCamioneta(usuariologueado, camionetaStore)
                chataModif = int(input("Que número de camioneta quiere modificar? "))
                nuevosKm = int(input("Cuantos Km tiene el vehiculo?: "))
                camionetaStore[chataModif].cambiarKM(nuevosKm)
                print(f"La camioneta quedo modificada con los siguientes datos: ", camionetaStore[chataModif].mostrar())
            elif categoriaProducto == 5:
                print(f"Colectivos en el concecionario: ")
                mostrarColectivo(usuariologueado, colectivoStore)
                coleModif = int(input("Que nùmero de colectivo desea modificar?: "))
                nuevosKm = int(input("Cuantos Km tiene el vehiculo?: "))
                colectivoStore[coleModif].cambiarKM(nuevosKm)
                print(f"El colectivo quedo modificado con los siguientes datos: ", colectivoStore[coleModif].mostrar())
            elif categoriaProducto == 6:
                print(f"Camiones en el concecionario: ")
                mostrarCamion(usuariologueado, camionStore)
                mioncaModif = int (input(" Que nùmero de camion quiere modificar?: "))
                nuevosKm = int (input("Cuantos KM tiene el vehiculo?: "))
                camionStore[mioncaModif].cambiarKM(nuevosKm)
                print(f"El camion que modificó quedo con los siguientes datos: ", camionStore[mioncaModif].mostrar())
                #El camion debe poder cambiar ademas si tiene acopado 
            elif categoriaProducto == 7:
                print(f"Acoplados en el concecionario: ")
                mostrarAcoplado(usuariologueado, acopladoStore)
                acopladoModif = int (input("Que número de acoplado desea modificar?: "))
                nuevosKm = int(input("Cuantos Km tiene el acoplado?: "))
                acopladoStore[acopladoModif].cambiarKM(nuevosKm)
                print(f"El acoplado quedo moficado con los siguientes datos: ", acopladoStore[acopladoModif].mostrar())
                #El acoplado debe poder cambiar si va con camion o no
            else: 
                print("No es una opcion correcta, intente nuevamente")
                menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
        elif opcEditar == 3:
            categoriaProducto = int(input('\nEDICION DETALLES Y OTROS DATOS \n MENU DE PRODUCTOS: \n 1. Autos \n 2. Motos \n 3. Bicicletas \n 4. Camionetas \n 5. Colectivos \n 6. Camiones \n 7.Acoplados \n \n INGRESE EL NUMERO DE LA OPCION DESEADA   \n'))
            if categoriaProducto == 1:
                print(f"Autos en el consecionario: ")
                mostrarAuto(usuariologueado, autoStore)
                autoModif = int(input("Que nùmero de auto desea modificar?: "))
                nuevosDatos =  int(input("Agregue el estado o dato adicional del vehiculo: "))
                autoStore[autoModif].cambiarEstado(nuevosDatos)
                print(f"El auto quedo modificado con los siguientes datos: ", autoStore[autoModif].mostrar())
            elif categoriaProducto == 2:
                print(f"Motos en el consecionario: ")
                mostrarMoto(usuariologueado, motoStore)
                motoModif = int(input("Que número de moto desea modificar?: "))
                nuevosDatos =  int(input("Agregue el estado o dato adicional del vehiculo: "))
                motoStore[motoModif].cambiarEstado(nuevosDatos)
                print(f"La moto que modifico quedo con los siguientes datos: ", motoStore[motoModif].mostrar())
            elif categoriaProducto == 3:
                print(f"Bicicletas en el consecionario: ")
                mostrarBici(usuariologueado, biciStore)
                biciModif = int(input("Que número de bicicleta desea modificar?: "))
                nuevosDatos =  int(input("Agregue el estado o dato adicional del vehiculo: "))
                biciStore[biciModif].cambiarEstado(nuevosDatos)
                print(f"La bicicleta que modifico quedo con los siguientes datos: ", motoStore[biciModif].mostrar())
            elif categoriaProducto == 4:
                print(f"Camionetas en el consecionario: ")
                mostrarCamioneta(usuariologueado, camionetaStore)
                chataModif = int(input("Que número de camioneta quiere modificar? "))
                nuevosDatos = int(input("Agregue el estado o dato adicional del vehiculo: "))
                camionetaStore[chataModif].cambiarEstado(nuevosDatos)
                print(f"La camioneta quedo modificada con los siguientes datos: ", camionetaStore[chataModif].mostrar())
            elif categoriaProducto == 5:
                print(f"Colectivos en el concecionario: ")
                mostrarColectivo(usuariologueado, colectivoStore)
                coleModif = int(input("Que nùmero de colectivo desea modificar?: "))
                nuevosDatos = int(input("Agregue el estado o dato adicional del vehiculo: "))
                colectivoStore[coleModif].cambiarEstado(nuevosDatos)
                print(f"El colectivo quedo modificado con los siguientes datos: ", colectivoStore[coleModif].mostrar())
            elif categoriaProducto == 6:
                print(f"Camiones en el concecionario: ")
                mostrarCamion(usuariologueado, camionStore)
                mioncaModif = int (input(" Que nùmero de camion quiere modificar?: "))
                nuevosDatos = int (input("Agregue el estado o dato adicional del vehiculo: "))
                camionStore[mioncaModif].cambiarEstado(nuevosDatos)
                print(f"El camion que modificó quedo con los siguientes datos: ", camionStore[mioncaModif].mostrar())
                #El camion debe poder cambiar ademas si tiene acopado 
            elif categoriaProducto == 7:
                print(f"Acoplados en el concecionario: ")
                mostrarAcoplado(usuariologueado, acopladoStore)
                acopladoModif = int (input("Que número de acoplado desea modificar?: "))
                nuevosDatos = int(input("Agregue el estado o dato adicional del vehiculo: "))
                acopladoStore[acopladoModif].cambiarEstado(nuevosDatos)
                print(f"El acoplado quedo moficado con los siguientes datos: ", acopladoStore[acopladoModif].mostrar())
                #El acoplado debe poder cambiar si va con camion o no
            else: 
                print("No es una opcion correcta, intente nuevamente")
                menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
        elif opcEditar == 4:
            menuOpciones(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore , camionStore, acopladoStore, camionetaStore, logueado)
        else: 
            print("No tiene acceso a esta opcion. ")



#Menu para CREAR 
def crearProductos(usuariologueado):
    print (" Aqui podra crear vehiculos \n ")
    categoriaProducto = int(input('MENU DE PRODUCTOS: \n 1. Autos \n 2. Motos \n 3. Bicicletas \n 4. Camionetas \n 5. Colectivos \n 6. Camiones \n 7.Acoplados \n \n INGRESE EL NUMERO DE LA OPCION DESEADA   \n'))
    if categoriaProducto == 1:
        crearAuto()
    if categoriaProducto == 2:
        crearMoto()
    if categoriaProducto == 3:
        crearBici()
    if categoriaProducto == 4:
        crearCamioneta()
    if categoriaProducto == 5:
        crearColectivo()
    if categoriaProducto == 6:
        crearCamion()
    if categoriaProducto == 7:
        crearAcoplado()

#Modificar usuario
def modificarUsuario(userData):
    print("Aqui podra modificar los usuarios")
    for u in userData["nombre"]:
        usuarioIndex = userData["nombre"].index(u)
        print(f"Usuario:",usuarioIndex, userData["nombre"][usuarioIndex], userData["usuario"][usuarioIndex], userData["permiso"][usuarioIndex] )
    usuarioModif = int(input("Ingrese el número de usuario que quiere modificarle el permiso: "))
    permisoNuevo = input("Los permisos admitidos son: \n Visita \n Empleado \n Admin\n Copie y pegue la opcion deseada \n")
    userData["permiso"][usuarioModif] = permisoNuevo
    print(f"El usuario ", userData["nombre"][usuarioModif], "quedo modificado de la siguiente forma:\n", "Usuario: ",userData["usuario"][usuarioModif], "\nPermiso: ", userData["permiso"][usuarioModif])



#----------------------------COLECTIVO----------------------------------------

def crearColectivo ():
        marca = input("Marca del colectivo: ")
        color = input ("Color del colectivo: ")
        motor = input ("Motor del colectivo: ")
        precio = input ("Precio de lista sin financiacion: ")
        pasajeros = input ("Que cantidad de pasajeros puede transportar: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        bondi = Colectivo(marca, color, motor, precio, pasajeros, km )
        colectivoStore.append(bondi)

def mostrarColectivo(usuariologueado , colectivoStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in colectivoStore:
            bondiIndex = colectivoStore.index(i)
            print("Colectivo  ", bondiIndex,":" , colectivoStore[bondiIndex].adminMostrar())
    else:
        for i in colectivoStore:
            bondiIndex = colectivoStore.index(i)
            print("Colectivo  ", bondiIndex,":" , colectivoStore[bondiIndex].mostrar())


def baseColectivo():
    bondiBase = Colectivo('Ford', 'gris', 'v8', '34', 0, 'Nuevo')
    colectivoStore.append(bondiBase)
    bondiBase = Colectivo('Mercedez', 'V8', 'V8', '34', 122311, 'Usado')
    colectivoStore.append(bondiBase)

#----------------------AUTOS------------------

def crearAuto():
        marca = input("Marca del auto: ")
        color = input ("Color del auto: ")
        motor = input ("Motor del auto: ")
        precio = input ("Precio de lista sin financiacion: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        estado = input("Comentario sobre el estado del auto: ")
        car = Auto(marca, color, motor, precio, km, estado)
        autoStore.append(car)

def mostrarAuto(usuariologueado , autoStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in autoStore:
            carIndex = autoStore.index(i)
            print("Auto  ", carIndex,":" , autoStore[carIndex].adminMostrar())
    else:
        for i in autoStore:
            carIndex = autoStore.index(i)
            print("Auto  ", carIndex,":" , autoStore[carIndex].mostrar())


def baseAuto():
    carBase = Auto ("Fiat", 'rojo', 'v8', '3400', 0, 'Nuevo')
    autoStore.append(carBase)
    carBase = Auto('Mercedez', 'negro', 'V8', '18786', 122311)
    autoStore.append(carBase)

#--------------------MOTOS-----------------------

def crearMoto():
        marca = input("Marca de la moto: ")
        color = input ("Color de la moto: ")
        motor = input ("Motor de la moto: ")
        precio = input ("Precio de lista sin financiacion: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        estado = input("Comentario sobre el estado de la moto: ")
        motico = Moto(marca, color, motor, precio, km, estado)
        motoStore.append(motico)

def mostrarMoto(usuariologueado , motoStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in motoStore:
            motoIndex = motoStore.index(i)
            print("Moto  ", motoIndex,":" , motoStore[motoIndex].adminMostrar())
    else:
        for i in motoStore:
            motoIndex = motoStore.index(i)
            print("Moto  ", motoIndex,":" , motoStore[motoIndex].mostrar())


def baseMoto():
    motoBase = Moto ("Yamaha", 'rojo', '1500', '3400', 0, 'Nuevo')
    motoStore.append(motoBase)
    motoBase = Moto ('Zanela', 'negro', '600', '18786', 122311)
    motoStore.append(motoBase)

#-----------------------------------BICICLETA--------------------------------

def crearBici():
        tipo = input("Tipo de bicicleta: ")
        rodado = input ("Rodado: ")
        estado= input ("Estado de la bici: ")
        precio = input ("Precio de lista sin financiacion: ")
        marca = input("marca de la bici: ")
        bici = Bicicleta(tipo, rodado , estado , precio , marca)
        biciStore.append(bici)

def mostrarBici(usuariologueado, biciStore):
    if usuariologueado["permiso"] == "Admin":
        print("ENTRE EN BICIS TRUE")
        for e in biciStore:
            biciIndex = biciStore.index(e)
            print("Bici  ", biciIndex,":" , biciStore[biciIndex].adminMostrar())
    else:
        print("ENTRE EN BICIS FALSE")
        for u in biciStore:
            biciIndex = biciStore.index(u)
            print("Bici  ", biciIndex,":" , biciStore[biciIndex].mostrar())
        

def baseBici():
    biciBase = Bicicleta("Paseo", '27', 'Usadita', '3400', "Mariela")
    biciStore.append(biciBase)
    biciBase = Bicicleta('Playera', '25', 'recien pintada', '18786')
    biciStore.append(biciBase)

#--------------------------CAMIONETA------------------------------------

def crearCamioneta():
        marca = input("Marca del camioneta: ")
        color = input ("Color del camioneta: ")
        motor = input ("Motor del camioneta: ")
        precio = input ("Precio de lista sin financiacion: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        estado = input("Comentario sobre el estado del camioneta: ")
        chata = Camioneta(marca, color, motor, precio, km, estado)
        camionetaStore.append(chata)

def mostrarCamioneta(usuariologueado , camionetaStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in camionetaStore:
            chataIndex = camionetaStore.index(i)
            print("Camioneta  ", chataIndex,":" , camionetaStore[chataIndex].adminMostrar())
    else:
        for i in camionetaStore:
            chataIndex = camionetaStore.index(i)
            print("Camioneta  ", chataIndex,":" , camionetaStore[chataIndex].mostrar())


def baseCamioneta():
    chataBase = Camioneta("Toyota", 'roja', 'v8', '3400', 0, 'Nuevo')
    camionetaStore.append(chataBase)
    chataBase = Camioneta('Ford', 'negra', 'V8', '18786', 122311)
    camionetaStore.append(chataBase)

#----------------------------CAMIONES---------------------------
def crearCamion():
        marca = input("Marca del camion: ")
        color = input ("Color del camion: ")
        motor = input ("Motor del camion: ")
        precio = input ("Precio de lista sin financiacion: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        estado = input("Comentario sobre el estado del camion: ")
        mionca = Camiones(marca, color, motor, precio, km, estado)
        camionStore.append(mionca)

def mostrarCamion(usuariologueado , camionStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in camionStore:
            mioncaIndex = camionStore.index(i)
            print("Camion  ", mioncaIndex,":" , camionStore[mioncaIndex].adminMostrar())
    else:
        for i in camionStore:
            mioncaIndex = camionStore.index(i)
            print("Camion ", mioncaIndex,":" , camionStore[mioncaIndex].mostrar())


def baseCamion():
    mioncaBase = Camiones ("Mecedez", 'blanco', 'v8', '3450', 0, 'Nuevo')
    camionStore.append(mioncaBase)
    mioncaBase = Camiones('Volvo', 'negro', 'V8', '18786', 122311)
    camionStore.append(mioncaBase)

#------------------------------ACOPLADOS----------------------------------------
def crearAcoplado():
        marca = input("Marca del camion: ")
        precio = input ("Precio de lista sin financiacion: ")
        km = int(input("Cuantos Km tiene el vehiculo: "))
        estado = input("Comentario sobre el estado del camion: ")
        acoplado = Acoplado(marca, precio, km, estado)
        acopladoStore.append(acoplado)

def mostrarAcoplado(usuariologueado , acopladoStore):
    if usuariologueado ["permiso"] == "Admin":
        for i in acopladoStore:
            acopladoIndex = acopladoStore.index(i)
            print("Acoplado  ", acopladoIndex,":" , acopladoStore[acopladoIndex].adminMostrar())
    else:
        for i in acopladoStore:
            acopladoIndex = acopladoStore.index(i)
            print("Acoplado ", acopladoIndex,":" , acopladoStore[acopladoIndex].mostrar())


def baseAcoplado():
    acopladoBase = Acoplado("Mecedez",'3450', 0, 'Nuevo')
    acopladoStore.append(acopladoBase)
    acopladoBase = Acoplado('Volvo', '18786', 122311)
    acopladoStore.append(acopladoBase)

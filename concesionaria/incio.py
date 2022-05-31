
from funciones import baseVehiculos,login, menuWelcome
from usuarios import colectivoStore, autoStore, crearUsuario , motoStore , biciStore, camionetaStore, camionStore, acopladoStore, userData


print("\nBienvenidos al concecionario de OsCar")
ingreso = int(input("\n Selecciones la opcion deseada: \n   1. Ingresar \n   2. Crear Usuario nuevo \n"))
if ingreso == 1:
    logueado, usuariologueado = login()
    intentos = 2
    while intentos != 0 and logueado == False:
        intentos -=1
        print(f'Usuario o contraseña incorrectos, intente nuevamente. Tiene {intentos} intentos antes que su cuenta se cierre.')
        logueado, usuariologueado = login()
        if logueado == False and intentos == 0:
            print('Su cuenta ha sido bloqueada')
else:
    crearUsuario()
    print("\nAhora puede ingresar al sistema\n")
    logueado, usuariologueado = login()
    intentos = 2
    while intentos != 0 and logueado == False:
        intentos -=1
        print(f'Usuario o contraseña incorrectos, intente nuevamente. Tiene {intentos} intentos antes que su cuenta se cierre.')
        logueado, usuariologueado = login()
        if logueado == False and intentos == 0:
            print('Su cuenta ha sido bloqueada')

if logueado:
    baseVehiculos()
    menuWelcome(usuariologueado, userData, autoStore, motoStore, biciStore, colectivoStore, camionStore, acopladoStore, camionetaStore, logueado)

#while logueado:
    #logueado = menuWelcome(usuariologueado,autoStore, motoStore, biciStore, colectivoStore)








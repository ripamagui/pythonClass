
class Camiones:
    def __init__(self, marca, color, motor, precio, km, estado = "Usado", acoplado='No posee acoplado'):
        self.marca = marca
        self.color = color 
        self.motor = motor 
        self.precio = precio
        self.km = km
        self.estado = estado
        self.acoplado = acoplado

    def mostrar(self):
        return self.marca, self. color, self.motor, self.km , self.estado , self.acoplado

    def adminMostrar(self):
        return self.marca, self. color, self.motor,  self.precio, self.km , self.estado , self.acoplado

    def cambiarKM(self, km):  #esto deberia agregarlo en todas las clases
        self.km = km
        #print('Se modifico el kilometraje a ', km)

    def cambiarPrecio(self,precio):
        self.precio = precio

    def cambiarEstado(self, estado):
        self.estado = estado
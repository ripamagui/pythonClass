
class Acoplado:
    def __init__(self, marca, precio, km, estado='Usado', camion='No posee camion'):
        self.marca = marca
        self.precio= precio 
        self.km = km
        self.estado = estado
        self.camion = camion

    def mostrar(self):
        return self.marca, self.km , self.estado , self. camion

    def adminMostrar(self):
        return self.marca, self. precio , self.km , self.estado , self. camion

    def cambiarKM(self, km):  #esto deberia agregarlo en todas las clases
        self.km = km
        #print('Se modifico el kilometraje a ', km)

    def cambiarPrecio(self, precio):
        self.precio = precio

    def cambiarEstado(self, estado):
        self.estado = estado

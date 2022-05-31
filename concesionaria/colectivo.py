#escolar = Colectivo('ford','naranja','f10',1200)
#print(escolar.marca)

class Colectivo:
    def __init__(self, marca, color, motor, precio, pasajeros, km, estado = "Usado") :
        self.marca = marca
        self.color = color 
        self.motor = motor
        self.precio = precio
        self.pasajeros = pasajeros
        self.km = km
        self.estado = estado

    def mostrar(self):
        return self.marca, self. color, self.motor, self.pasajeros, self.km , self.estado

    def adminMostrar(self):
        return self.marca, self. color, self.motor, self.precio, self.pasajeros, self.km , self.estado

    def cambiarKM(self, km):  #esto deberia agregarlo en todas las clases
        self.km = km
        #print('Se modifico el kilometraje a ', km)

    def cambiarPrecio(self,precio):
        self.precio = precio

    def cambiarEstado(self, estado):
        self.estado = estado







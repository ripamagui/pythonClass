

class Moto:
    def __init__(self, marca, color, motor, precio, km, estado = "Usado") :
        self.marca = marca
        self.color = color 
        self.motor = motor
        self.precio = precio
        self.km = km
        self.estado = estado

    def mostrar(self):
        return self.marca, self. color, self.motor, self.km , self.estado
    def adminMostrar(self):
        return self.marca, self. color, self.motor, self.precio, self.km , self.estado

    def cambiarKM(self, km):  
        self.km = km
        #print('Se modifico el kilometraje a ', km)

    def cambiarPrecio(self,precio):
        self.precio = precio

    def cambiarEstado(self, estado):
        self.estado = estado
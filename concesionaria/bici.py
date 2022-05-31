class Bicicleta:
    def __init__(self,tipo, rodado, estado, precio, marca="Sin Especificar"):
        self.tipo= tipo
        self.rodado= rodado
        self.estado =estado
        self.precio = precio
        self.marca = marca

    def mostrar(self):
        return self.tipo , self.rodado, self.estado , self.marca

    def adminMostrar(self):
        return self.tipo , self.rodado, self.estado , self.precio , self.marca

    def cambiarPrecio(self,precio):
        self.precio = precio

    def cambiarEstado(self, estado):
        self.estado = estado

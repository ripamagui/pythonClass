


class Colectivo:
    def __init__(self, marca, color, motor, precio, km, pasajeros, estado = "Usado") :
        self.marca = marca
        self.color = color 
        self.motor = motor
        self.estado = estado
        self.precio = precio
        self.km = None
        self.pasajeros = pasajeros

    def cambiarKM (self, km):  #esto deberia agregarlo en todas las clases
        self.km = km

    def crearColectivo ():
        brand = input("Marca del colectivo: ")
        colour = input ("Color del colectivo: ")
        engine = input ("Motor del colectivo: ")
        price = input ("Precio de lista sin financiacion: ")
        passenger = input ("Que cantidad de pasajeros puede transportar: ")
        bondi = Colectivo(brand,colour,engine,price,passenger)
        colectivo.append(bondi)
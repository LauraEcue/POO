class Auto:
    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

    def describir(self):
        return f"Auto {self.marca} de color {self.color}"    



# Probar lo que hicimos
mi_auto = Auto("Toyota", "Rojo", 4)
print(mi_auto.describir())

class Telefono:
    def __init__(self, marca, tamaño, modelo, color):
        self.marca = marca
        self.tamaño = tamaño
        self.modelo = modelo
        self.color = color

    def describir(self):
        return f"mi telefono {self.marca} de color {self.color}, es de {self.tamaño}"

 # probar lo que hice
mi_telefono = Telefono("motorola", "17cm", "Model 2017", "blanco")
print(mi_telefono.describir())


class Estudiante:
    def __init__(self, nombre, apellido, cedula, estatura):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.estatura = estatura

#probar lo que hice
mi_compañero = Estudiante("laura", "castillo", 1081398452, 1.59)
print(f"nombre: {mi_compañero.nombre}")
print(f"apellido: {mi_compañero.apellido}")
print(f"cedula: {mi_compañero.cedula}")
print(f"estatura: {mi_compañero.estatura}")        



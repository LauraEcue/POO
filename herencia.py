class Persona:
    def __init__(self, nombre: str, apeliido: str, email: str ):
        self.nombre = nombre
        self.apellido = apeliido
        self.email = email

    def describir(self) :
        print(f"{self.nombre} {self.apellido}")

class Profesor(Persona):
    def __init__(
            self, nombre: str, apellido: str, email: str, profesion: str, maestria: str ):
        super().__init__(nombre, apellido, email)
        self.profesion = profesion
        self.maestria = maestria

#probar
profesor1 = Profesor("Luis", "Gutierrez", "luisgutierrez@gmail.com", "Ingeniero agronomo", "Maestria en recursos agricolas")
profesor1.describir()

profesor2 = Profesor("Julio", "Diaz", "juliodiaz@gmail.com", "Fisico", "Matematicas")
profesor2.describir()



class Empleado(Persona):
    def __init__(
            self, nombre: str, apellido: str, email: str, cedula: int, cargo: str, salario: int):
        super().__init__(nombre, apellido, email)
        self.cedula = cedula
        self.cargo = cargo
        self.salario = salario

#probar
empleado1 = Empleado("Jhon", "Figueroa", "lui@gmail.com", 109766, "administrador", 2000000)
empleado1.describir()

class Doctor(Persona):
    def __init__(
            self, nombre: str, apellido: str, email: str, cargo: str, especialidad: str):
        super().__init__(nombre, apellido, email)
        self.cargo = cargo
        self.especialidad = especialidad

#probar
doctor1 = Doctor("Juan", "Lopez", "juan@gmail.com", "Medico general", "Anestesiologo")
doctor1.describir()





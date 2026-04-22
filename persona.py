class Persona:
    def __init__(self, nombre: str, edad: int, cedula: str,):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
   

    def categoria(self):
        if self.edad < 12:
            return "pertenezco al grupo de niños."
        elif self.edad <= 28:
            return "pertenezo al grupo de jovenes"
        else:
            return "pertenezco al grupo de adulto mayor"
        

    def describir(self) -> str:
        return f"Hola, soy {self.nombre}, tengo {self.edad} años, mi cedula es {self.cedula},"

#prueba
persona = Persona("Laura Castillo", 20, "1081324564",)
print(persona.describir(), persona.categoria())

persona = Persona("Jeison gallego", 50, "12342134",)
print(persona.describir(), persona.categoria())


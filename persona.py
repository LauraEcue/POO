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
Laura = Persona("Laura Castillo", 20, "1081324564",)
print(Laura.describir(), Laura.categoria())

Jeison = Persona("Jeison gallego", 50, "12342134",)
print(Jeison.describir(), Jeison.categoria())

Luis = Persona("Luis Gutierrez", 23, "1120435432",)
print(Luis.describir(), Luis.categoria())

Julian = Persona("Julian Lopez", 10, "123124235",)
print(Julian.describir(), Julian.categoria())


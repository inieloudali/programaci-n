class Persona:
    nombre=""
    edad=0
    ciudad=""
    def saludar(self):
        return "hola"
    
    def presentarse(self):
        return f"mi nombre es {self.nombre}, vivo en {self.ciudad}, y tengo {self.edad}"

humano = Persona()
humano.nombre="Ivi"
humano.edad=16
humano.ciudad="Bs As"

print(humano.saludar())
print(humano.presentarse())


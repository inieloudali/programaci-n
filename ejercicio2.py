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



humano2 = Persona()
humano2.nombre="Gian"
humano2.edad=19
humano2.ciudad="Cordoba Capital"

print(humano.saludar())
print(humano.presentarse())

print(humano2.saludar())
print(humano2.presentarse())
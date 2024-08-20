class videojuego:

    def __init__ (self,titulo,plataformas,online,precio):
        
        self.titulo = titulo
        self.plataformas = plataformas
        self.online = online
        self.precio = precio

    def descripcion(self):
        if self.online==True:
            return f"El juego {self.titulo} esta disponible en {self.plataformas}, es un juego online y tiene un precio de {self.precio}"
        elif self.online==False:
            return f"El juego {self.titulo} esta disponible en {self.plataformas}, es un juego offline y tiene un precio de {self.precio}"


minecraft = videojuego("minecraft", "pc", True, "20")
valorant = videojuego("valorant","pc",True,"0")
hollow_knight = videojuego("hollow knight", "play/pc", False, "25")

print(minecraft.titulo)
print(minecraft.plataformas)
print(minecraft.online)
print(minecraft.precio)

print("------------------------------")

print(valorant.titulo)
print(valorant.plataformas)
print(valorant.online)
print(valorant.precio)

print("------------------------------")

print(hollow_knight.titulo)
print(hollow_knight.plataformas)
print(hollow_knight.online)
print(hollow_knight.precio)

print("------------------------------")

print(minecraft.descripcion())
print(valorant.descripcion())
print(hollow_knight.descripcion())
class planta_:
    def __init__(self,nombre,tipo,necesidad_de_agua):
        self.nombre=nombre
        self.tipo=tipo
        self.necesidad_de_agua=necesidad_de_agua

    def regar(self):
        cant_Agua=int(input("ingrese una cantidad de agua en ml"))
        if cant_Agua>self.necesidad_de_agua:
            return "me ahogo de tanta agua"
        elif cant_Agua==self.necesidad_de_agua:
            return "suficiente agua crack"
        else:
            return "me muerooooooo"
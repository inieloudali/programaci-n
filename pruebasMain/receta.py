class receta_:
    def __init__(self,nombre,ingredientes,tiempo_de_preparacion):
        self.nombre=nombre
        self.ingredientes=ingredientes
        self.tiempo_de_preparacion=tiempo_de_preparacion 
        
    def añadir_ingredientes(self):
        cant_ingredientes=int(input("Ingrese la cantidad de ingredientes de la receta"))
                              
        self.ingredientes=[]
        for x in range (0,cant_ingredientes):
            self.ingredientes.append(input("añade un ingrediente"))
        return self.ingredientes
    def mostrar_receta(self):
        return self.ingredientes


        


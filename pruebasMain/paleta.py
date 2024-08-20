class PaletaColores:
    def __init__(self,nombre,colores):
        self.nombre=nombre
        self.colores=colores
    def añadir_color(self):
        cantColores=int(input("ingrese la cantidad de colores que quiere: "))
        self.colores=[]
        for x in range(1,cantColores+1):
            self.colores.append(input(f"ingrese el color {x}: "))
        return self.colores
    
    def quitar_color(self):
        cantColores=int(input("ingrese la cantidad de colores que quiere eliminar: "))
        self.colores=[]
        a=""
        for x in range(1,cantColores+1):
            a=input("ingrese un color a eliminar: ")
            self.colores.remove(a)
        return self.colores
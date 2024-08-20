class Alarma:
    hora = 0
    activado = False 
    
    def configurar_alarma(self):
        self.hora=int(input("Ingrese la hora que quiere: "))
        return self.hora
    
    def activar_alarma(self):
        if self.hora>0:
            self.activado=True
        return self.activado, "La alarma esta activada"
    
    def desactivar_alarma(self):
        self.activado=False
        return self.activado, "la alarma esta desactivada"
    

alarma1=Alarma()
alarma1.hora=0
alarma1.activado=True

print(alarma1.configurar_alarma())
print(alarma1.desactivar_alarma())
print(alarma1.activar_alarma())
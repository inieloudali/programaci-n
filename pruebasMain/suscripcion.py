class suscripcion_:
    
    def __init__(self, servicio, costo_mensual, activo):
        self.servicio = servicio
        self.costo_mensual = costo_mensual
        self.activo = activo
    
    def activar(self):
        self.activo = True
        return self.activo

    def cancelar(self):
        self.activo = False
        return self.activo
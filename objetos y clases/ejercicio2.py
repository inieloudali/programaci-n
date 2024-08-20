class TarjetaDeCredito:
    numero=0
    titular=""
    saldo=0
    activa=False 

    def pagar(self):
        return f"la tarjeta numero {self.numero} de {self.titular} tiene {self.saldo}"
    
    def activar(self): 
        self.activa=True
        return self.activa
    
    def desactivar(self): 
        self.activa=False
        return self.activa
    
tarjeta1 = TarjetaDeCredito()
tarjeta1.numero = 123
tarjeta1.titular = "pepe"
tarjeta1.saldo=321
tarjeta1.activa=False

print(tarjeta1.activar())
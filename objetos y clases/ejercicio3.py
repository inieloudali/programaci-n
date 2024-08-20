class Gato:
    Nombre=""
    edad=0

    def maullar(self):
        return "miau"
    
    def cumplir_años(self):
        self.edad=self.edad+1
        return self.edad
    

gato1=Gato()
gato1.Nombre="Seba"
gato1.edad=3


class Estudiante:
    nombre=""
    matricula=""
    curso=[]
   
    
    def inscribirCurso(self):
        str=""
        cantCurso=int(input("ingrese la cantidad de curso a la que quiere aplicar: "))
        for x in range(1,cantCurso+1):
            str=input(f"ingrese el curso {x} al que quiere aplicar: ")
            self.curso.append(str)
        return self.curso
      
    def listar_curso(self):
        return self.curso
    

Estudiante1=Estudiante()
Estudiante1.nombre="juan"
Estudiante1.matricula="no se que tendría que ir aca"
Estudiante1.curso=[]

Estudiante1.inscribirCurso()
print(Estudiante1.listar_curso())
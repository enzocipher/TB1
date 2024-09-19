import random
#crear equipos
class Team:
    def __init__(self, nombre):
        self.nombre = nombre
    ganadas= 0; perdidas=0; empatadas = 0
    def setSuma(self):
        self.ganadas+=1
    def setResta(self):
        self.perdidas += 1
    def setEmpate(self):
        self.empatadas += 1
#registrarlos

uno = Team("enzo")
uno.setSuma()
uno.setSuma()
print(uno.nombre, uno.ganadas)

pass
def verificador(inicio, fin, valor ):
    if valor<inicio or valor > fin:
        return False
    else: return True


def registroequipos(arregloprincipal):
    cantidad = 0
    while verificador(1, 20, cantidad) == False:
        cantidad = int(input("Ingrese cantidad a generar"))
    for i in range(0, cantidad):
        currentteam = Team(input("Ingrese nombre del equipo"))
        arregloprincipal.append(currentteam)

#Stand by
def escupirequipos(arreglo):
    contador = 0; contador2 = 1
    print("\t", end="")
    for i in range(3):
        print("Partido ", i+1, "\t", end = "")
    print("")
    for i in range(len(arreglo)):
        if contador == 0:
            print("Dia ", contador2, "\t", end=""); contador2+=1
        print(arreglo[i].nombre, end = " ")
        if contador == 5:
            print(""); contador=0;
        if (i+1)%2!=0:
            print(" VS ", end = " ")
        else:
            print("\t", end="")
        contador+=1
        

def aleatorio(equipo):
    resultadopartido = random.randint(1, 3)
    match resultadopartido:
        case 1: resutadopartido = "Ganado"; equipo.ganada+=1
        case 2: resultadopartido = "Perdido"; equipo.perdidas+=1
        case 3: resultadopartido = "Empate"; equipo.empatadas+=1
    return resultadopartido

    
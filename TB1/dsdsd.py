def funciondentro(contadorespacios):
        for i in range(0, contadorespacios*2):
            print(" ", end = "")

def funciondentro2(contadorespacios, i):
        for j in range(0, contadorespacios*2+2):
            print(i, end = "")

def funcion(n):
    if n%2 == 0:
        mitad = n/2
    else:
        mitad = ((n+1)/2)
    contadorespacios = n-1 
    contadorespacioinicial = 1
    for i in range(0,n):
        
        if contadorespacioinicial == mitad:
            for j in range(contadorespacioinicial-1):
                print(" ", end = "")
        else:
            for i in range(contadorespacioinicial):
                print(" ", end = "")
        contadorespacioinicial+=1
        print(i+1, end = "")
        if (i == mitad-1):
             funciondentro2(contadorespacios, i+1)
        else : funciondentro(contadorespacios)
        if(i != n-1): print(i+1)
        contadorespacios-=1

n = int(input("Ingrese un numero"))
funcion(n)

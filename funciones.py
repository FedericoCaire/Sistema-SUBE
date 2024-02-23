def descuento(x): #Descuento Por Tarifa Social
        return x*0.45

def recargo(x): #Recargo Por No Registrar Sube
        return x*1.58

def genero(x):
    match x:
        case 0:
            return "Masculino"
        case 1:
            return "Femenino"
        case 2:
            return "X"
         

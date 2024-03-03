from validaciones import dni_valido,genero_valido,apynom_valido,mail_valido,fecha_valida
from mensajes import msj_carga_exitosa
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

def numero_genero(genero):
     match genero:
        case "Masculino":
            return 0
        case "Femenino":
            return 1
        case "X":
            return 2
               
def eliminar_espacios_inicio_fin(palabra):
    inicio = 0
    fin = len(palabra)-1
    while (inicio<=len(palabra)-1) and (palabra[inicio]==" "): inicio = inicio + 1
    while (fin>=0) and (palabra[fin]==" "): fin = fin - 1
    return palabra[inicio:fin+1]

def pedir_dni():
    dni = input("ingrese DNI: ")
    valido = dni_valido(dni)
    while valido==False:
       print(" ")
       print("DNI invalido vuelva a ingresarlo correctamente")
       dni = input("ingrese DNI: ")
       valido= dni_valido(dni)
    return dni

def pedir_apynom():
    apellido = eliminar_espacios_inicio_fin(input("ingrese apellido: ").lower())
    while apynom_valido(apellido)==False:
       print(" ")
       print("Apellido invalido vuelva a ingresarlo correctamente")
       apellido = eliminar_espacios_inicio_fin(input("ingrese apellido: ").lower())
    
    nombre = eliminar_espacios_inicio_fin(input("ingrese nombre: ").lower())
    while apynom_valido(nombre)==False:
       print(" ")
       print("Apellido invalido vuelva a ingresarlo correctamente")
       nombre = eliminar_espacios_inicio_fin(input("ingrese nombre: ").lower())

    return apellido + " " + nombre

def pedir_fecha():
    fecha = input("ingrese su fecha de nacimiento(DD/MM/YYYY): ")
    while fecha_valida(fecha)==False:
        print(" ")
        print("Fecha invalida vuelva a ingresarla correctamente")
        fecha = input("ingrese su fecha de nacimiento(DD/MM/YYYY): ")
    return fecha

def pedir_mail():
    mail = input("ingrese Correo Electronico: ")
    while mail_valido(mail)==False:
        print(" ")
        print("Mail invalido vuelva a ingresarlo correctamente")
        mail = input("ingrese Correo Electronico: ")
    return mail

def pedir_genero():
    genero = input("ingrese genero(Masculino/Femenino/X): ")
    while genero_valido(genero)==False:
        print(" ")
        print("Genero invalido vuelva a escribir correctamente una de las opciones")
        genero = input("ingrese genero(Masculino/Femenino/X): ")
    return numero_genero(genero)

def tramo_colectivo(distancia):
    if distancia<=3:
        return 0
    elif distancia>3 and distancia<=6:
        return 1
    elif distancia>6 and distancia<=12:
        return 2
    elif distancia>12 and distancia<=27:
        return 3
    else:
        return 4
    
def pedir_opcion(cant_opciones):
    try:
        opc = int(input("Ingrese una opcion: "))
    except:
        print("Ingrese una opcion valida")
        return pedir_opcion()
    if opc>=1 and opc<=cant_opciones:
        return opc
    else:
        print("Ingrese una opcion valida")
        return pedir_opcion()
    
def pedir_carga():
    try:
        return float(input("Ingrese la carga: "))
    except:
        print("Ingrese un numero valido")
        return pedir_carga()

def pedir_distancia():
    try:
        distancia = int(input("Indique la distancia (en km) a realizar: "))
    except:
        print("Ingrese un numero valido")
        return pedir_distancia()
    if distancia>=0:
        return distancia
    else:
        print("Ingrese un numero valido")
        return pedir_distancia()
    
def pedir_tramo_tren():
    try:
        tramo = int(input("Indique el tramo que realizara(1,2 o 3): "))
    except:
        print("Ingrese un numero valido")
        return pedir_tramo_tren()
    if tramo>=1 and tramo<=3:
        return tramo-1
    else:
        print("Ingrese un numero valido")
        return pedir_tramo_tren()

mostrar_saldo = lambda sube: print(f"Su saldo actual es de: {sube.get_saldo()}")

def cargar_sube(sube):
    carga = pedir_carga()
    sube.cargar_tarjeta(carga)
    msj_carga_exitosa()
    mostrar_saldo(sube)










         

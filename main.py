from funciones import descuento, recargo, genero, pedir_dni, pedir_apynom, pedir_fecha, pedir_genero, pedir_mail, tramo_colectivo, pedir_distancia, pedir_opcion, mostrar_saldo, cargar_sube

VALOR_PASAJE_COLECTIVO = [270,301,323,347,370]
VALOR_PASAJE_SUBTE = 757
VALOR_PASAJE_TREN = [130,169,208]
SALDO_NEGATIVO_MAXIMO = -480

class TarjetaNoRegistrada:
    def __init__(self,numero,saldo):
        self.__numero = numero
        self.__saldo = saldo
        self.__baja = False

    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,nuevo_saldo):
        self.__saldo = nuevo_saldo 

    def get_baja(self):
        return self.__baja
    def set_baja(self):
        self._baja = not self._baja

    def registrar_tarjeta(self):
        dni = pedir_dni()
        apynom = pedir_apynom()
        fecha_nacimiento = pedir_fecha()
        genero = pedir_genero()
        mail = pedir_mail()
        print(" ")
        print("sube registrada correctamente")
        return TarjetaRegistrada(self.get_numero(),self.get_saldo(),apynom,dni,fecha_nacimiento,genero,mail,False)
    
    def cargar_tarjeta(self,carga):
        nuevo_saldo = self.get_saldo() + carga
        self.set_saldo(nuevo_saldo)
    
    def viaje_colectivo(self,i):
        nuevo_saldo = self.get_saldo() - recargo(VALOR_PASAJE_COLECTIVO[i])
        self.set_saldo(nuevo_saldo)

    def saldo_disponible(self,valor_pasaje):
        if (self.get_saldo()-valor_pasaje)>=SALDO_NEGATIVO_MAXIMO:
            return True
        else:
            return False


class TarjetaRegistrada(TarjetaNoRegistrada):
    def __init__(self,numero,saldo,apynom,dni,fecha_nacimiento,genero,mail,descuento):
        super().__init__(numero,saldo)
        self.__apynom = apynom
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento
        self.__genero = genero
        self.__mail = mail
        self.__descuento = descuento

    def get_apynom(self):
        return self.__apynom
    def set_apynom(self,nuevo_apynom):
        self.__apynom = nuevo_apynom

    def get_dni(self):
        return self.__dni
    def set_dni(self,nuevo_dni):
        self.__dni = nuevo_dni

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def set_fecha_nacimiento(self,nueva_fecha_nacimiento):
        self.__fecha_nacimiento = nueva_fecha_nacimiento
    
    def get_genero(self):
        return genero(self.__genero)
    def set_genero(self,nuevo_genero):
        self.__genero= nuevo_genero
    
    def get_mail(self):
        return self.__mail
    def set_mail(self,nuevo_mail):
        self.__mail = nuevo_mail

    def get_descuento(self):
        return self.__descuento
    def set_descuento(self):
        self._descuento = not self._descuento

    def viaje_colectivo(self,i):
        if self.get_descuento()==True:
            nuevo_saldo = self.get_saldo() - descuento(VALOR_PASAJE_COLECTIVO[i])
        else:
            nuevo_saldo = self.get_saldo() - VALOR_PASAJE_COLECTIVO[i]
        self.set_saldo(nuevo_saldo)

    def consulta_datos_tarjeta(self):
        print("DNI: ", self.get_dni())
        print("Apellido y Nombre: ", self.get_apynom())
        print("Fecha de nacimiento: ", self.get_fecha_nacimiento())
        print("Genero: ", self.get_genero())
        print("Correo Electronico: ", self.get_mail())
        print("Tarifa Social: Si") if self.get_descuento()==True else print("Tarifa Social: No")
    
def crear_tarjeta():
    return TarjetaNoRegistrada("6061268506072830",float(0))

def menu_sube_no_registrada(sube):
    def volver_a_menu(sube):
        print(" ")
        input("presione ENTER para volver al menu anterior")
        print(" ")
        menu_sube_no_registrada(sube)
        

    print("1. Registrar Sube")
    print("2. Cargar Sube")
    print("3. Ver Saldo")
    print("4. Viajar")
    print("5. Salir")
    print(" ")
    opc = pedir_opcion()
    match opc:
        case 1:
            print(" ")
            sube = sube.registrar_tarjeta()
            print(" ")
            menu_sube_registrada(sube)
        case 2:
            cargar_sube(sube)
            volver_a_menu(sube)
        case 3:
            mostrar_saldo(sube)
            volver_a_menu(sube)
        case 4:
            print(" ")
            distancia = pedir_distancia()
            tramo = tramo_colectivo(distancia)
            sube.viaje_colectivo(tramo)
            print(" ")
            print("Pago realizado")
            mostrar_saldo(sube)
            volver_a_menu(sube)
        case 5:
            pass

def menu_sube_registrada(sube):
    def volver_a_menu(sube):
        print(" ")
        input("presione ENTER para volver al menu anterior")
        print(" ")
        menu_sube_registrada(sube)
        
    print("1. Ver Datos Personales")
    print("2. Cargar Sube")
    print("3. Ver Saldo")
    print("4. Viajar")
    print("5. Salir")
    print(" ")
    opc = pedir_opcion()
    match opc:
        case 1:
            print(" ")
            sube.consulta_datos_tarjeta()
            print(" ")
            volver_a_menu(sube)
        case 2:
            cargar_sube(sube)
            volver_a_menu(sube)
        case 3:
            mostrar_saldo(sube)
            volver_a_menu(sube)
        case 4:
            pass
        case 5:
            pass
    

    




sube = crear_tarjeta()
menu_sube_no_registrada(sube)
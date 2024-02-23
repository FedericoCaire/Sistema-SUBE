from funciones import descuento, recargo, genero

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
        dni = input("ingrese DNI: ")
        apynom = input("ingrese Apellido y Nombre: ")
        fecha_nacimiento = input("ingrese Fecha de nacimiento(dd/mm/yyyy): ")
        genero = input("ingrese genero(1: Masculino/2: Femenino/3: X): ")
        mail = input("ingrese Correo Electronico: ")
        print("sube registrada correctamente")
        return TarjetaRegistrada(self.get_numero(),self.get_saldo(),apynom,dni,fecha_nacimiento,genero,mail,False)
    
    def cargar_tarjeta(self,carga):
        nuevo_saldo = self.get_saldo() + carga
        self.set_saldo(nuevo_saldo)
    
    def viaje_colectivo(self):
        valor_pasaje = 215
        nuevo_saldo = self.get_saldo() - recargo(valor_pasaje)
        self.set_saldo(nuevo_saldo)


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

    def viaje_colectivo(self):
        valor_pasaje = 215
        if self.get_descuento()==True:
            nuevo_saldo = self.get_saldo() - descuento(valor_pasaje)
        else:
            nuevo_saldo = self.get_saldo() - valor_pasaje
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


sube = crear_tarjeta()
tarjeta_registrada = sube.registrar_tarjeta()
print(" ")
tarjeta_registrada.viaje_colectivo()
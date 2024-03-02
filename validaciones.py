def es_numero(x):
     if x=="0":
          return True
     elif x=="1":
          return True 
     elif x=="2":
          return True 
     elif x=="3":
          return True 
     elif x=="4":
          return True 
     elif x=="5":
          return True 
     elif x=="6":
          return True 
     elif x=="7":
          return True 
     elif x=="8":
          return True 
     elif x=="9":
          return True 
     else:
          return False
     
def es_letra(x):
     if x=="a":
          return True
     elif x=="b":
          return True
     elif x=="c":
          return True
     elif x=="d":
          return True
     elif x=="e":
          return True
     elif x=="f":
          return True
     elif x=="g":
          return True
     elif x=="h":
          return True
     elif x=="i":
          return True
     elif x=="j":
          return True
     elif x=="k":
          return True
     elif x=="l":
          return True
     elif x=="m":
          return True
     elif x=="n":
          return True
     elif x=="ñ":
          return True
     elif x=="o":
          return True
     elif x=="p":
          return True
     elif x=="q":
          return True
     elif x=="r":
          return True
     elif x=="s":
          return True
     elif x=="t":
          return True
     elif x=="u":
          return True
     elif x=="v":
          return True
     elif x=="w":
          return True
     elif x=="x":
          return True
     elif x=="y":
          return True
     elif x=="z":
          return True
     else:
          return False
         
def dni_valido(dni): 
    if len(dni)>=7 and len(dni)<=8:
        i = 0
        encontrado = False
        while i<len(dni) and encontrado==False:
            if es_numero(dni[i])==False: encontrado = True 
            i = i+1
        return not encontrado
    else:
        return False

def apynom_valido(apynom):
     if len(apynom)>=3 and len(apynom)<=100:
          i = 0
          encontrado = False
          while i<len(apynom) and encontrado==False:
               if (es_letra(apynom[i])==False) and (not apynom[i]==" "):
                    encontrado = True
               i = i+1
          return not encontrado
     else:
          return False

def genero_valido(genero):
     genero = genero.lower()
     if genero=="masculino" or genero=="femenino" or genero=="x": return True 
     else: return False

def mail_valido(mail):
     if len(mail)>=5:
          i = 0
          encontrado = False
          while (i<=len(mail)-1) and (encontrado==False):
               if mail[i]=="@": encontrado = True
               i = i+1
          return encontrado
     else:
          return False

def fecha_valida(fecha):
     def forma_fecha_valida(fecha):
          if len(fecha)==10:
               i = 0
               invalido = False
               while (i<=9) and (invalido==False):
                    if i!=2 and i!=5:
                         invalido = not es_numero(fecha[i])
                    else:
                         invalido = fecha[i]!="/"
                    i = i+1
               return not invalido
          else:
               return False
     def anio_biciesto(anio):
          if (anio%100)!=0:
               return (anio%4)==0
          else:
               return (anio%400)==0
     
     if forma_fecha_valida(fecha)==True:
          dia = int(fecha[:2])
          mes = int(fecha[3:5])
          anio = int(fecha[6:])

          if (dia >= 1) and (dia <= 31) and (mes >= 1) and (mes <= 12) and (anio >= 1900) and (anio <= 2024):
               if (mes in [1,3,5,7,8,10,12])==True:
                    return dia<=31
               elif (mes in [4,6,9,11]):
                    return dia<=30
               elif mes==2:
                    if anio_biciesto(anio)==True:
                         return dia<=29
                    else:
                         return dia<=28
          else: return False
     else: return False

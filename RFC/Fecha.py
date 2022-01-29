"""Esta clase sirva para definir fechas""" 
class Fecha:
    def __init__(self, dia_nacimiento, mes_nacimiento, año_nacimiento):
        '''Rutina para definir los dias'''
        if (dia_nacimiento >= 27 and dia_nacimiento<= 31):
            self.__dia_nacimiento = dia_nacimiento
            #print(f"El nuevo dia de nacimiento es: {self.__dia_nacimiento}") 
        else:
            print("ERROR !!! EL DIA DE NACIMIENTO QUE COLOCASTE NO PUEDE SER VUELVE A CARGAR LA INFORMACION")
        
        '''Rutina para definir los meses'''
        meses_del_año = {1 : "Enero", 2: "Febrero", 3 : "Marzo", 4 : "Abril", 5 : "Mayo", 6 :"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
        if (mes_nacimiento >=1 and mes_nacimiento <= 12):
            self.__mes_nacimiento = mes_nacimiento
            #print(f"Tu nuevo mes de nacimiento es: {meses_del_año[self.__mes_nacimiento]}")           
           
        else:
            print("ERROR !!! EL MES DE NACIMIENTO QUE COLOCASTE NO PUEDE SER VUELVE A CARGAR LA INFORMACION")
            
        '''Rutina para definir los años'''
        if (año_nacimiento >= 1900 and año_nacimiento <= 2021):
            self.__año_nacimiento = año_nacimiento
            #print(f"Tu nuevo año de nacimiento es: {self.__año_nacimiento}")
        elif (año_nacimiento <= 1900):
            print("No pudiste nacer antes de 1900 estas muerto lol")
        elif (año_nacimiento >= 2021):
            print(f"Apoco vienes del futuro no manches que naciste despues del 2021")
        
        #self.__dia_nacimiento = dia_nacimiento
        #self.__mes_nacimiento = mes_nacimiento
        #self.__año_nacimiento = año_nacimiento

    @property
    def dia_nacimiento(self):
        #print(f"El dia de nacimiento es: {self.__dia_nacimiento}")
        return str(self.__dia_nacimiento)
    @dia_nacimiento.setter
    def dia_nacimiento(self, dia_nacimiento):
        if (dia_nacimiento >= 27 and dia_nacimiento<= 31):
            self.__dia_nacimiento = dia_nacimiento
            print(f"El nuevo dia de nacimiento es: {self.__dia_nacimiento}") 
        else:
            print("ERROR !!! EL DIA DE NACIMIENTO QUE COLOCASTE NO PUEDE SER VUELVE A CARGAR LA INFORMACION")
       
    @property
    def mes_nacimiento (self):
        meses_del_año = {1 : "01-Enero", 2: "02-Febrero", 3 : "03-Marzo", 4 : "04-Abril", 5 : "05-Mayo", 6 :"06-Junio", 7:"07-Julio", 8:"08-Agosto", 9:"09-Septiembre", 10:"10-Octubre", 11:"11-Noviembre", 12:"12-Diciembre"}
        #print(f"El mes de nacimiento es: {meses_del_año[self.__mes_nacimiento]}")
        return meses_del_año[self.__mes_nacimiento]
        
    @mes_nacimiento.setter
    def mes_nacimiento(self,mes_nacimiento):
        meses_del_año = {1 : "01-Enero", 2: "02-Febrero", 3 : "03-Marzo", 4 : "04-Abril", 5 : "05-Mayo", 6 :"06-Junio", 7:"07-Julio", 8:"08-Agosto", 9:"09-Septiembre", 10:"10-Octubre", 11:"11-Noviembre", 12:"12-Diciembre"}
        if (mes_nacimiento >=1 and mes_nacimiento <= 12):
            self.__mes_nacimiento = mes_nacimiento
            print(f"El nuevo mes de nacimiento es: {meses_del_año[self.__mes_nacimiento]}")           
           
        else:
            print("ERROR !!! EL MES DE NACIMIENTO QUE COLOCASTE NO PUEDE SER VUELVE A CARGAR LA INFORMACION")  
    
    @property
    def año_nacimiento(self):
        #print(f"El año de nacimiento es: {self.__año_nacimiento} ")
        return str(self.__año_nacimiento)
    @año_nacimiento.setter
    def año_nacimiento(self,año_nacimiento):
        if (año_nacimiento >= 1900 and año_nacimiento <= 2021):
            self.__año_nacimiento = año_nacimiento
            print(f"El nuevo año de nacimiento es: {self.__año_nacimiento}")
        elif (año_nacimiento >= 1900):
            print("No pudiste nacer antes de 1900 estas muerto lol")
        elif (año_nacimiento <= 2021):
            print(f"Apoco vienes del futuro no manches que naciste despues del 2021")

    
   



if __name__ == '__main__': 
    cumpleaños = Fecha(28,7,1995)
    """cumpleaños.dia_nacimiento = 28
    cumpleaños.mes_nacimiento
    cumpleaños.mes_nacimiento = 2
    cumpleaños.mes_nacimiento
    cumpleaños.año_nacimiento
    cumpleaños.año_nacimiento = 1800
    cumpleaños.año_nacimiento = 3000
    cumpleaños.año_nacimiento = 1994
    cumpleaños = Fecha(28,7,1800)
    dia = cumpleaños.dia_nacimiento
    mes = cumpleaños.mes_nacimiento
    año = cumpleaños.año_nacimiento
    print(dia+mes+año)"""

  


    

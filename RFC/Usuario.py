from Persona import Persona

class Usuario(Persona):

    def __init__(self, nombre, primer_apellido, segundo_apellido, dia_nacimiento, mes_nacimiento, año_nacimiento):
        super().__init__(nombre, primer_apellido, segundo_apellido, dia_nacimiento, mes_nacimiento, año_nacimiento)
    
    def mostrar_datos(self):
        nombre = self.nombre
        primer_apellido = self.primer_apellido
        segundo_apellido = self.segundo_apellido
        dia_nacimiento = self.dia_nacimiento
        mes_nacimiento = self.mes_nacimiento
        año_nacimiento = self.año_nacimiento
        
        print("Tus datos de usuario son los siguientes:"+
              "\nEl nombre es: "+nombre+
              "\nEl primer apellido es: "+ primer_apellido+
              "\nEL segundo apellido es: "+segundo_apellido+
              "\nEl dia de nacimiento es: "+dia_nacimiento+
              "\nEl mes de nacimiento es: "+mes_nacimiento+
              "\nEl año de nacimiento es: "+año_nacimiento)
        
    
    def generar_RFC(self):
        #Carrillo
        iniciales_primer_apellido = self.primer_apellido[0:2]
        #Garcia
        iniciales_segundo_apellido = self.segundo_apellido[0:2]
        #Erick
        iniciales_nombre = self.nombre[0]
        #1995
        año_nacimiento = self.año_nacimiento[2:4]
        #07
        mes_nacimiento = self.mes_nacimiento[0:2]
        #28
        dia_nacimiento = self.dia_nacimiento

        rfc = iniciales_primer_apellido + iniciales_segundo_apellido + iniciales_nombre + año_nacimiento + mes_nacimiento + dia_nacimiento

        '''print(iniciales_primer_apellido)
        print(iniciales_segundo_apellido)
        print(iniciales_nombre)
        print(año_nacimiento)
        print(mes_nacimiento)
        print(dia_nacimiento)'''
        print("Tu RFC es el siguiente: "+ rfc.upper())
      

        

    
        

if __name__ == '__main__':
    erick = Usuario("Erick","Carrillo","Garcia",28,7,1995)
    erick.mostrar_datos()
    erick.generar_RFC()
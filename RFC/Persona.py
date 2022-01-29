"""Esta clase nos ayuda a crear nombres con apellidos"""
from  Fecha import Fecha
class Persona(Fecha):
    #declero el metodo constructor junto con las variables de la clase
    def __init__(self,nombre, primer_apellido, segundo_apellido,dia_nacimiento, mes_nacimiento, año_nacimiento): 
        #utilizo el metodo self para hacer referencia al los objetos
        super().__init__(dia_nacimiento, mes_nacimiento, año_nacimiento)
        self.__nombre = nombre
        self.__primer_apellido = primer_apellido
        self.__segundo_apellido = segundo_apellido
    #funcion getter del nombre
    @property
    def nombre (self):
        #print("El nombre es: "+ self.__nombre)
        return self.__nombre
    #funcion setter del nombre
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        print("El nuevo nombre es: "+ self.__nombre)
    @property
    def primer_apellido(self):
        #print("El primer apellido es: "+ self.__primer_apellido)
        return self.__primer_apellido
    @primer_apellido.setter
    def primer_apellido (self, primer_apellido):
        self.__primer_apellido = primer_apellido
        print("El nuevo primer apellido es: "+ self.__primer_apellido)
    @property
    def segundo_apellido(self):
        #print ("El segundo apellido es: "+ self.__segundo_apellido)
        return self.__segundo_apellido
    @segundo_apellido.setter
    def segundo_apellido(self, segundo_apellido):
        self.__segundo_apellido = segundo_apellido
        print("El nuevo segundo apellido es:" + self.__segundo_apellido)
    
    

if __name__ == '__main__':
    """erick = Persona("Erick","Carrillo","Garcia",28,7,1995)
    nombre = erick.nombre
    apellido_1 = erick.primer_apellido 
    apellido_2 = erick.segundo_apellido
    print(nombre+apellido_1+ apellido_2)"""





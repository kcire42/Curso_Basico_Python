# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:47:09 2020

@author: erick.carrillo

"""

class Celular:
    def __init__(self, marca, modelo, cantidad_camaras):
        self.marca = marca
        self.modelo = modelo
        self.camara  = Camara(cantidad_camaras)
        
    
        
    def informacion (self):
        print(f"El celular que esta en funcionamiento es de marca{self.marca}, modelo{self.modelo} y cuenta con {cantidad_camaras[0]} camaras")
        
       
        
class Camara:
    def __init__(self,cantidad_camaras):
        self._cantidad_camaras = cantidad_camaras 
        
    @property 
    def numero_camaras(self):
        if self._cantidad_camaras <= 4:
            return self._cantidad_camaras, True
        else:
            return self._cantidad_camaras, False
    @numero_camaras.setter
    def set_numero_camaras(self, cantidad_camaras):
        self._cantidad_camaras = cantidad_camaras
        
            
        
        
    
    def seleccion_camara(self, camara_seleccionada):
        if camara_seleccionada == 1: #and camara_seleccionada <= self.cantidad_camaras:
            print(f"El zoom esta en x{camara_seleccionada*10}")
            Camara.accion_camara()
        elif camara_seleccionada ==2: #and camara_seleccionada <= self.cantidad_camaras:
            print(f"El zoom esta en x{camara_seleccionada*10}")
            Camara.accion_camara()
        elif camara_seleccionada ==3: #and camara_seleccionada <= self.cantidad_camaras:
            print(f"El zoom esta en x{camara_seleccionada*10}")
            Camara.accion_camara()
        elif camara_seleccionada ==4: #and camara_seleccionada <= self.cantidad_camaras:
            print(f"El zoom esta en x{camara_seleccionada*10}")
            Camara.accion_camara()
        else:
            print("Error al seleccionar la camara")
    
    def accion_camara():
        menu = """
        1- Tomar foto
        2- Tomar video
        """
        print(menu)
        accion = int(input("Ingrese la opcion deasada: "))
        if accion == 1:
            print("Se a tomado la foto Pummm!!!!")
        elif accion == 2:
            print("Se grabo el video")
        else:
            print("Error")
    def informacion (self):
        print(f"El celular que esta en funcionamiento es de marca{self.marca}, modelo{self.modelo}")

class contactos:
    pass

class memoria:
    pass

        
        
if __name__ == '__main__':
    note10 = Celular("Samsung", "Galaxy Note 10",4)
    #validacion modelo creado
    cantidad_camaras = note10.camara.numero_camaras
    print(cantidad_camaras[1]) 
    if cantidad_camaras[1] == True:
        print("La cantidad de camaras fue dada de alta correctamente")
    else:
        note10.camara.set_numero_camaras = int(input("Ingrese el numero de camaras menor o igual a 4"))
    note10.informacion()
    
    camara_seleccionada = int(input("Seleccione que camara quiere usar:"))
note10.camara.seleccion_camara(camara_seleccionada)
    
  
    

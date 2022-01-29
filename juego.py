# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:21:51 2020

@author: erick.carrillo
"""
import random

def juego():
    contador = 0
    vidas = 0
    numero_a_advinar = int(random.randint(0,10))
    numero_a_advinar_str = str(numero_a_advinar)
    print("El numero correcto es: "+numero_a_advinar_str)
    #numero_a_advinar = 1
    while vidas < 3:
        numero = int(input("Ingrese un numero del 1 al 100: "))
        
        
        if numero == numero_a_advinar:
            contador += 1
            break
        else:
            vidas += 1
    numero_a_advinar = str(numero_a_advinar)
    if contador == 0:
         print("Haz Perdido el numero correcto era: "+ numero_a_advinar)
    if contador == 1:
         print("Haz Ganado el numero correcto era: "+ numero_a_advinar)
     
            
        


if __name__ == '__main__':
     juego()
    #print(random.randint(0,10))
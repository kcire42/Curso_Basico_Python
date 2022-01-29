# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:48:12 2020

@author: erick.carrillo
"""
import random
import collections

palos = ['picas','corazon','rombo','trebol']
valores = ['as','2','3','4','5','6','7','8','9','10','joto','reina','rey']

def crear_baraja():
    barajas = []
    for palo in palos:
        for valor in valores:
            barajas.append((palo,valor))
    return barajas

def obtener_mano (barajas,tamaño_de_mano):
    mano = random.sample(barajas,tamaño_de_mano)
    return mano
    
def main(tamaño_de_mano, intentos):
    barajas = crear_baraja()
    manos = []  
    for numero_de_manos in range(intentos):
        mano = obtener_mano(barajas,tamaño_de_mano)
        manos.append(mano)
    pares = 0
    tercia = 0
    full = 0
    
    for mano in manos:
        valores = []
        #print(mano)
        for carta in mano:
        
            #print (carta[0])
            #print (carta[1])
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        print(f'los valores del counter{counter}')
        for val in counter.values():
        
            #print(val)
            if val  == 2:
                pares += 1
                break
            if val == 3:
                tercia += 1
                continue
        if  pares > 0 and tercia > 0:
                full += 1   
    probabilidad_par = (pares / intentos)*100
    probabilidad_tercia = (tercia/intentos)*100
    probabilidad_full = (full/intentos)*100
    print(f'Se obtuvieron {pares} pares de las manos que se sacaron La probabilidad de obtener un para es de {probabilidad_par}%')
    print(f'Se obtuvieron {tercia} tercia de las manos que se sacaron La probabilidad de obtener un para es de {probabilidad_tercia}%')
    print(f'Se obtuvieron {full} full de las manos que se sacaron La probabilidad de obtener un para es de {probabilidad_full}%')   
    #print(manos)
    
        
    

if __name__ == '__main__':
    tamaño_de_mano = int(input('Ingrese el tamaño de la mano: '))
    intentos = int(input('Ingrese cuantos intentos quiere realizar: '))
    main(tamaño_de_mano,intentos)
    
   
    
    
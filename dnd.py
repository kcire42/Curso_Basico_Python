# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 01:10:30 2020

@author: erick.carrillo
"""

class Character:
    def __init__(self, user,name,level,life_points):
        self.user = user
        self.name = name
        self.level = 0 
        self.life_points = life_points
        
               
    def front(self,unidades):
        print(f"Te haz movido {unidades} unidades hacia enfrente")
    def rear(self,unidades):
        print(f"Te haz movido {unidades} unidades hacia atras")
    def left(self,unidades):
        print(f"Te haz movido {unidades} unidades hacia la izquierda")
    def right(self,unidades):
        print(f"Te haz movido {unidades} unidades hacia la derecha")
    def atack_basic(self):
        print(f"Haz realizado un ataque basico")
    def atack_special(self):
        print(f"Haz realizado un ataque especial")
        
        


class Half_elf(Character):
    def __init__(self,user,name,level,life_points,name_class, magic_points, type_magic):
        super().__init__(user,name,level,life_points)
        self.name_class = "Half_Elf"
        self.magic_points = 15
        self.type_magic = type_magic
        
    def hyper_jump(self):
        print(f"Haz realizado un salto de 10 unidades")
    def fire_ball(self):
        print(f"Lanzaste bola de fuego")
    def atack_special(self):
        print("Dragon Claw")
        
if __name__ == '__main__':
    kcire = Half_elf("kcire","kcire",0,15,"Half_Elf",15,"Fire")
    safari = Character("miltonvdg","safari",0,25)
    kcire.front(10)
    kcire.left(5)
    kcire.front(10)
    print("Ha aparecido un mounstro")
    kcire.rear(3)
    kcire.hyper_jump()
    kcire.front(1)
    kcire.fire_ball()
    kcire.atack_special()
    safari.atack_special()
    
    



    
        
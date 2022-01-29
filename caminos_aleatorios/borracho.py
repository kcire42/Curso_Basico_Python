import random

class Borracho:
    def __init__(self,nombre): #metodo construtor
        self.nombre = nombre
    

class BorrachoTradicional(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])

class BorrachoEspacial(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
    def camina(self):
        return random.choice([(2,3),(2,-3),(2,3),(-2,3)])

class BorrachoLoco(Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)
    def camina(self):
        return random.choice([(0,4),(0,-4),(4,5),(-4,5)])
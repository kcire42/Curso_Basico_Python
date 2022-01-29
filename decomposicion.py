class Automovil:
    def __init__(self.modelo,marca,color):
        self.modelo = modelo 
        self.marca = marca
        self.color = color 
        self._estado = 'en reposo'
        self.motor = Motor(cilindros=4)
    
    def acelerar(self,tip='despacio'):
        if tipo == 'rapida':
            self.Motor.inyecta_gasolina(10)#va lento
        else:
            self.Motor.inyecta_gasolina(3)#va rapido
        self._estado = 'en movimiento'

class Motor:
    def __init__(self. cilindros, tipo = 'gasolina', caballos_de_fuerza):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0 
        self.caballos_de_fuerza = caballos_de_fuerza
    def inyecta_gasolina(self,litro_gasolina):
        pass

#PROGRAMA QUE TE DICE UNA RAIZ CUADRADA
def run():
    numero = int(input("Ingrese un numero: "))
    respuesta = 0
    while respuesta**2 < numero:
        #multiplicacion = respuesta**2
        #print(f'Para cuando respuesta vale {respuesta} su numero elevado a cuadrado es {multiplicacion}')
        respuesta +=1
    #print(f'Para cuando respuesta vale {respuesta} su numero elevado a cuadrado es {respuesta**2}')
    if respuesta**2 == numero:
        print(f'La raiz cuadrada de {numero} es {respuesta} y es exacta')
    else:
        raiz = numero**(1/2)
        raiz = str(raiz)
        print(f'El numero {numero} no tiene raiz exacta pero su raiz es {raiz}')
        
    
if __name__ == '__main__':
    run()
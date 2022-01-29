def run():
    objetivo = int (input('Escoge un numero: '))
    epsilon = 0.1
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo)>= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2)-objetivo,respuesta)
        respuesta +=paso
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz cudrada {objetivo}')
    else:
        print(f'la raiz cuadrada del {objetivo} es la siguiente {respuesta}')

if __name__ == '__main__':
    run()

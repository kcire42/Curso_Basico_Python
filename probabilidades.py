import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    for _ in range(numero_de_tiros):
        dado_1 = random.choice([1,2,3,4,5,6])
        dado_2 = random.choice([1,2,3,4,5,6])
        tiro = dado_1 + dado_2
        secuencia_de_tiros.append(tiro)
    #print(secuencia_de_tiros)
    return secuencia_de_tiros

def main(numero_de_tiros,numero_de_intentos):
    tiros= []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    print(f'El array de los dados es: {tiros}')
    tiros_con_1= 0 
    tiros_con_12 = 0
    for tiro in tiros:
        if 6 in tiro:
            tiros_con_1 += 1
        if 12 in tiro:
            tiros_con_12 += 1
    probabilidad_de_tiros_con_1 = tiros_con_1/numero_de_intentos
    probabilidad_de_tiros_con_12 = tiros_con_12/numero_de_intentos
    print(f'La probabilidad de que haya un tiro con 1 es de {probabilidad_de_tiros_con_1} y hubo un total de {tiros_con_1} numeros 1')
    print(f'La probabilidad de que haya un tiro con 12 es de {probabilidad_de_tiros_con_12} y hubo un total de {tiros_con_12} numeros 12')

if __name__ == '__main__':
    #numero_de_dados = int(input(f'Ingrese el numero de dados: '))
    numero_de_tiros = int(input(f'Ingrese el numero de tiros: '))
    numero_de_intentos = int(input(f'Ingrese el numero de pruebas que quiere realizar: '))
    main(numero_de_tiros,numero_de_intentos)
        
def suma(numero_1, numero_2):
    resultado = numero_1+numero_2
    return resultado


if __name__ == '__main__':
    numero_1 = int(input("Ingrese un numero: "))
    numero_2 = int(input("Ingrese un numero: "))
    print(f'El resultado de la suma es: {suma(numero_1,numero_2)}')
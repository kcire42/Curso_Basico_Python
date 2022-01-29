import sys
def fibonacci_recursiva(n):
    if n == 0 or n ==1 :
        return 1
    return fibonacci_recursiva(n-1)+fibonacci_recursiva(n-2)

def fibonacci_dinamica(n,memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado =  fibonacci_dinamica(n-1,memo)+fibonacci_dinamica(n-2,memo)
        memo[n] = resultado
        return resultado 




if __name__ == '__main__':
    sys.setrecursionlimit(10100)
    n = int(input("Ingrese un numero del cual quiere obtener fibonacci: "))
    resultado = fibonacci_dinamica(n)
    print(resultado)
    
edad = int(input("Coloca tu edad: "))
if edad < 18:
    print("Eres menor de edad")cd 
elif edad >= 18 and edad < 25:
    print("Eres adulto joven")
elif edad >= 25 and edad < 60:
    print("Eres señor")
elif edad >= 60 and edad < 120:
     print("tercera edad")
else:
    print("Te moriste")
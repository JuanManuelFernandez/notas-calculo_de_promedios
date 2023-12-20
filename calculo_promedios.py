"""calculo de promedios"""

import tkinter as tk



def tres_notas():
    nota1 = int(input("ingrse su nota: "))

    nota2 = int(input("ingrese su segunda nota: "))

    nota3 = int(input("ingrese su tercer nota: "))

    promedio = (nota1 + nota2 + nota3) / 3

    print(promedio)

def cinco_notas():
    nota1 = int(input("ingrese su primer nota: "))

    nota2 = int(input("ingrese su segunda nota: "))

    nota3 = int(input("ingrese su tercer nota: "))

    nota4 = int(input("ingrese su cuarta nota: "))

    nota5 = int(input("ingrese su quinta nota: "))

    promedio2 = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

    print(promedio2)

while True:
    opciones = int(input("ingrese la opción: "))
    if opciones == 1:
        tres_notas()
        break
    elif opciones == 2:
        cinco_notas()
        break
    else:
        print("opción no disponible, se agregaran más en el futuro")
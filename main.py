import os
import string
import time


import Miselanea
flagM: bool
mise = Miselanea.Miselanea
var: string

menup = """
Bienvenidos a la micelanea de Pyton,a continuación selecione 
la opción de su prefiera:
[1] Operadores 
[2] Condicionales
[3] Ciclos 
[99] Salir
"""

menuo = """
Bienvenidos a la micelanea de Pyton,a continuación selecione 
la opción de su prefiera:
[1] área de un triángulo.
[2] Suma de dos números.
[3] calcular el cuadrado de un número.
[4] calculo de euros a dólares.
[5] Calculo del área y del perímetro de un cuadrado.
[6] Calcular el área y el volúmen de un cilindro.
[7] Calcular longitud el área de un circulo.
[8] Calcular el promedio de tres (3) números .
[9] Regresar.
[99] Salir.
"""

menuc = """
Bienvenidos a la micelanea de Pyton,a continuación selecione 
la opción de su prefiera:
[1] saber si el número ingresado por teclado es positivo o negativo.
[2] Evaluar  dos números y diga cuál es el mayor y cuál el menor.
[3] Ingrese tres números enteros positivos y que calcule e imprima en
    pantalla el menor y el mayor de ellos.
[4] Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.
[5] Calculo del área y del perímetro de un cuadrado.
[6] Calcular el área y el volúmen de un cilindro.
[7] Ingrese dos números , sumarlos si al menos uno de ellos es negativo, en caso contrario
    multiplicarlos.
[8] Calcular el promedio de tres (3) números .
[9] Regresar.
[99] Salir.
"""

menuci = """
Bienvenidos a la micelanea de Pyton,a continuación selecione 
la opción de su prefiera:
[1] saber si el número ingresado por teclado es positivo o negativo.
[2] Evaluar  dos números y diga cuál es el mayor y cuál el menor.
[3] Ingrese tres números enteros positivos y que calcule e imprima en
    pantalla el menor y el mayor de ellos.
[4] Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.
[5] Calculo del área y del perímetro de un cuadrado.
[6] Calcular el área y el volúmen de un cilindro.
[7] Ingrese dos números , sumarlos si al menos uno de ellos es negativo, en caso contrario
    multiplicarlos.
[8] Calcular el promedio de tres (3) números .
[9] Regresar.
[99] Salir.
"""


def operadores() -> object:
    os.system('cls')
    print(menuo)
    opcion = int(input("Introduce la opcion: "))

    while True:
        if opcion == 1:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce la base del triangulo: "))
                h = int(input("Introduce la altura del trangulo: "))
                mise.area_triangulo(b, h)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            operadores()

        elif opcion == 2:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce el primer número: "))
                h = int(input("Introduce el segundo número: "))
                mise.sumaAB(b, h)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 3:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce el número que quiere elevar al cuadrado: "))
                mise.potencia(b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 4:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Ingrese los la cantidad de Dolares que desea cambiar: "))
                mise.convercion(b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 5:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el valor del lado del cuadrado: "))
                mise.apcuadrado(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()

        elif opcion == 6:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el radio del cilindro: "))
                h = int(input("Ingrese la altura del cilindor: "))
                mise.avcilindro(r, h)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 7:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el radio del circunferencia: "))
                mise.alcircunferencia(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 8:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                x = int(input("Ingrese el primer número: "))
                y = int(input("Ingrese el segundo número: "))
                z = int(input("Ingrese el tercer número: "))
                mise.promedio()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            operadores()
        elif opcion == 9:
            pmenu(var)
        elif opcion == 99:
            print('Gracias por usar nuestros servicios hasta luego')
            exit()
        else:
            print('Por favor digite una opcion correcta')
            time.sleep(2)
            operadores()


def condicionales():
    os.system("cls")
    print(menuc)
    opcion = int(input("Introduce la opcion: "))

    while True:
        if opcion == 1:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce el número q desea evaluer: "))
                mise.negativopositivo(x)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            operadores()

        elif opcion == 2:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce el primer número: "))
                h = int(input("Introduce el segundo número: "))
                mise.mayormenor2(b, h)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 3:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                b = int(input("Introduce el número que quiere elevar al cuadrado: "))
                mise.potencia(b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 4:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo múmero: "))
                mise.suma2(a,b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 5:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el valor del lado del cuadrado: "))
                mise.apcuadrado(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()

        elif opcion == 6:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo múmero: "))
                mise.suma3(a, b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 7:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el radio del circunferencia: "))
                mise.alcircunferencia(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 8:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                x = int(input("Ingrese el primer número: "))
                y = int(input("Ingrese el segundo número: "))
                z = int(input("Ingrese el tercer número: "))
                mise.promedio()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            condicionales()
        elif opcion == 9:
            pmenu(var)
        elif opcion == 99:
            print('Gracias por usar nuestros servicios hasta luego')
            exit()
        else:
            print('Por favor digite una opcion correcta')
            time.sleep(2)
            condicionales()

def ciclos():
    os.system("cls")
    print(menuc)
    opcion = int(input("Introduce la opcion: "))

    while True:
        if opcion == 1:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                mise.multipos3()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            ciclos()

        elif opcion == 2:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                mise.impares()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 3:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                mise.pares()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 4:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                mise.cuadrados30()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO)"))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 5:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el valor del lado del cuadrado: "))
                mise.apcuadrado(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            ciclos()

        elif opcion == 6:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                a = int(input("Ingrese el primer número: "))
                b = int(input("Ingrese el segundo múmero: "))
                mise.suma3(a, b)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 7:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                r = int(input("Ingrese el radio del circunferencia: "))
                mise.alcircunferencia(r)
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 8:
            flag: int = 2
            op: int
            while flag == 2:
                os.system('cls')
                x = int(input("Ingrese el primer número: "))
                y = int(input("Ingrese el segundo número: "))
                z = int(input("Ingrese el tercer número: "))
                mise.promedio()
                op = int(input("Desea regresar al menu anterior 1(SI) 2(NO): "))
                if op == 1:
                    flag = 1
            ciclos()
        elif opcion == 9:
            pmenu(var)
        elif opcion == 99:
            print('Gracias por usar nuestros servicios hasta luego')
            exit()
        else:
            print('Por favor digite una opcion correcta')
            time.sleep(2)
            ciclos()



def pmenu(var):
    flagM = True
    os.system('cls')
    print(menup)
    opcion = int(input("Introduce la opcion: "))

    while True:
        if opcion == 1:
            operadores()
        elif opcion == 2:
            condicionales()
        elif opcion == 3:
            ciclos()
        elif opcion == 99:
            print('Gracias por usar nuestros servicios hasta luego')
            exit()
        else:

            print('Por favor digite una opcion correcta')
            time.sleep(2)
            os.system("cls")
            pmenu("cls")


if __name__ == '__main__':
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    pmenu(var)
import math
import string


class Miselanea:
    a: float
    conv: float

    @staticmethod
    def area_triangulo(b, h):
        a = (b * h) / 2

        return print("El area del trinagulo de base {} y altura {} es: {}".format(b, h, a))

    @staticmethod
    def sumaAB(x, y):
        suma = x + y
        return print("La suma de {} y {} es: {}".format(x, y, suma))

    @staticmethod
    def potencia(x):
        p = (x ** 2)
        return print('El cuadrado de {} es: {}'.format(x, p))

    @staticmethod
    def convercion(us) -> object:
        conv = format((us * 1.10), '.2f')
        return print('Por {} US recivira {} EUR '.format(us, conv))

    @staticmethod
    def apcuadrado(lado) -> object:
        ar = lado ** 2
        per = lado * 4
        return print(
            'El area del cuadrado de lado ' + lado + 'su area es: ' + str(ar) + ' y su perimetro es' + str(per))

    @staticmethod
    def avcilindro(r, h) -> object:
        ar = round(2 * math.pi * r * (h + r), 2)
        vol = round(math.pi * (r ** 2) * h, 2)
        return print('Para un cilindro de altura ' + str(h) + ' y radio ' + str(r) + ' su area es: ' + str(
            ar) + ' y su volumen es: ' + str(vol))

    @staticmethod
    def alcircunferencia(r) -> object:
        ar = round((math.pi * (r ** 2)), 2)
        lon = round(2 * math.pi * r, 2)

        insert_var = "Para una circunferencia de radio  {} su area es: {} y su longitud es: {}".format(r, ar, lon)
        return print(insert_var)

    @staticmethod
    def promedio(x, y, z) -> object:
        prom = round((x + y + z) / 3, 2)

        insert_var = "El promedio de los numeros {},{} y {} es: {}".format(x, y, z, prom)

        # print
        print(insert_var)

    @staticmethod
    def negativopositivo(x) -> object:
        if x > 0:
            print("El número {} es positivo.".format(x))
        elif x < 0:
            print("El número {} negativo".format(x))

    @staticmethod
    def mayormenor2(x, y) -> object:
        mayor = x
        if mayor > y:
            menor = y
        elif mayor < y:
            menor = mayor
            mayor = y

        print("El número {} es mayor y el número {} es menor.".format(mayor, menor))

    @staticmethod
    def mayormenor3(x, y, z) -> object:
        mayor = x
        if mayor > y:
            menor = y
        elif mayor < y:
            menor = mayor
            mayor = y

        print("El número {} es mayor y el número {} es menor.".format(mayor, menor))

    @staticmethod
    def suma2(a, b) -> object:
        resultado:int
        mensaje:string

        if a < b:
            resultado=a+b
            mensaje= (" la operacion {} + {} es igual a {}.".format(a, b,resultado))
        elif a>b:
            resultado= a-b
            mensaje= (" la operacion {} - {} es igual a {}.".format(a, b,resultado))

        return print(mensaje)

    @staticmethod
    def suma3(a, b) -> object:
        resultado: int
        mensaje: string

        if a < 0 or b<0:
            resultado = a + b
            mensaje = (" la operacion {} + {} es igual a {}.".format(a, b, resultado))
        else:
            resultado = a * b
            mensaje = (" la operacion {} * {} es igual a {}.".format(a, b, resultado))

        return print(mensaje)


    @staticmethod
    def multipos3() -> object:
        j: int
        j=3

        for x in range(100):
            x += 1

            if (x%3==0):
                print(str(x))

    @staticmethod
    def impares() -> object:
        j: int
        j=3

        for x in range(100):


            if (x%2!=0):
                print(str(x))


    @staticmethod
    def cuadrados30() -> object:
        j: int
        i = 1
        while i < 31:
            j = (i ** 2)
            print("{}: {}".format(i,j))
            i += 1

    @staticmethod
    def sumacuadrados100() -> object:
        j: int
        i = 1
        while i < 100:
            j = (i ** 2)
            print("{}: {}".format(i,j))
            i += 1










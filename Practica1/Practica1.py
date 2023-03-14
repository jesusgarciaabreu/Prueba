import math
import string
import random
import turtle
from fractions import Fraction

def DiferenciadorDeNumeros(lista):
    i = 0
    while(i < len(lista)):
        j = i + 1
        while(j < len(lista)):
            if(lista[i] == lista[j]):
                return False
            j += 1
        i += 1
    return True

def MediaMuestral(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma / len(lista)

def Varianza(lista):
    guardaElemento = 0.0
    sumaFinal = 0.0
    for i in lista:
        guardaElemento = i - MediaMuestral(lista)
        guardaElemento = guardaElemento**2
        sumaFinal = sumaFinal + guardaElemento
    return sumaFinal / len(lista) - 1

def DesviacionEstandar(lista):
    return math.sqrt(Varianza(lista))

def HazLista(temperaturas):
    mi_archivo = open(temperaturas, 'r')
    lista_temperaturas = []
    for line in mi_archivo.readlines():
        line = float(line)
        lista_temperaturas.append(line)
    mi_archivo.close()
    return lista_temperaturas

def Minimo():
    lista = HazLista("temperaturas.txt")
    minimo = lista[0]
    for i in lista:
        if(minimo > i):
            minimo = i
    return minimo

def Promedio():
    lista = HazLista("temperaturas.txt")
    promedio = 0
    numero_elementos = 0
    suma_elementos = 0
    for i in lista:
        suma_elementos +=  i
        numero_elementos += 1
    promedio = suma_elementos / numero_elementos
    return promedio

"""
* OTRA FORMA DE SACAR EL PROMEDIO.
def Promedio2(temperaturas):
    mi_archivo = open(temperaturas, 'r')
    suma_elementos = 0
    numero_elementos = 0
    promedio = 0
    for line in mi_archivo.readlines():
        line = float(line)
        numero_elementos += 1
        suma_elementos = suma_elementos + line
    promedio = suma_elementos / numero_elementos
    mi_archivo.close()
    return promedio
"""

def Maximo():
    lista = HazLista("temperaturas.txt")
    maximo = lista[0]
    for i in lista:
        if(maximo < i):
            maximo = i
    return maximo

def DiccionarioTemperaturas():
    diccionario = {"Minimo: ": Minimo(), "Promedio: ": Promedio(), "Maximo: ": Maximo()}
    return diccionario

def CadenasAleatorias():
    cadenaAleatoria = ""
    for i in range(28):
        espacio = random.randint(1, 5)
        if (espacio == 1):
            cadenaAleatoria = cadenaAleatoria +  " "
        else:
            cadenaAleatoria = cadenaAleatoria + random.choice(string.ascii_letters)
    cadenaAleatoria = cadenaAleatoria.lower()
    return cadenaAleatoria

def Coincidencias(cadenaAux):
    cadena1 = cadenaAux
    #print(cadena1)
    cadena2 = "methinks it is like a weasel"
    coincidencias = 0
    i = 0
    while(i < 28):
        if(cadena1[i] == cadena2[i]):
            coincidencias += 1
        i += 1
    return coincidencias

def MonoInfinito(digitos):
    cadenaFinal = ""
    while True:
        cadenaFinal = CadenasAleatorias()
        if(Coincidencias(cadenaFinal) == digitos):
            return cadenaFinal

def DibujarTriangulo(puntos,color,miTortuga):
    miTortuga.fillcolor(color)
    miTortuga.up()
    miTortuga.goto(puntos[0][0],puntos[0][1])
    miTortuga.down()
    miTortuga.begin_fill()
    miTortuga.goto(puntos[1][0],puntos[1][1])
    miTortuga.goto(puntos[2][0],puntos[2][1])
    miTortuga.goto(puntos[0][0],puntos[0][1])
    miTortuga.end_fill()

def ObtenerMitad(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def Sierpinski(puntos,grado,miTortuga):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    DibujarTriangulo(puntos,colormap[grado],miTortuga)
    if grado > 0:
        Sierpinski([puntos[0],
                        ObtenerMitad(puntos[0], puntos[1]),
                        ObtenerMitad(puntos[0], puntos[2])],
                   grado-1, miTortuga)
        Sierpinski([puntos[1],
                        ObtenerMitad(puntos[0], puntos[1]),
                        ObtenerMitad(puntos[1], puntos[2])],
                   grado-1, miTortuga)
        Sierpinski([puntos[2],
                        ObtenerMitad(puntos[2], puntos[1]),
                        ObtenerMitad(puntos[0], puntos[2])],
                   grado-1, miTortuga)

def TrianguloSierpinski():
   miTortuga = turtle.Turtle()
   miVentana = turtle.Screen()
   misPuntos = [[-100,-50],[0,100],[100,-50]]
   Sierpinski(misPuntos,3,miTortuga)
   miVentana.exitonclick()

def DibujoBase(dibuja, posicion1, posicion2):
    dibuja.penup()
    dibuja.goto(posicion1[0], posicion1[1])
    dibuja.pendown()
    dibuja.goto(posicion2[0], posicion2[1])


def PasoRecursivo(dibuja, x, y, largo, altura, contador):
    DibujoBase(dibuja, [x + largo * 0.25, altura // 2 + y], [x + largo * 0.75, altura // 2 + y])
    DibujoBase(dibuja, [x + largo * 0.25, (altura * 0.5) // 2 + y], [x + largo * 0.25, (altura * 1.5) // 2 + y])
    DibujoBase(dibuja, [x + largo * 0.75, (altura * 0.5) // 2 + y], [x + largo * 0.75, (altura * 1.5) // 2 + y])

    #CASO BASE
    if(contador <= 0):
        return
    #CASO RECURSIVO
    else: 
        contador -= 1
        # ARRIBA A LA IZQUIERDA
        PasoRecursivo(dibuja, x, y, largo // 2, altura // 2, contador)
        # ARRIBA A LA DERECHA
        PasoRecursivo(dibuja, x + largo // 2, y, largo // 2, altura // 2, contador)
        # ABAJO A LA IZQUIERDA
        PasoRecursivo(dibuja, x, y + largo // 2, largo // 2, altura // 2, contador)
        # ABAJO A LA DERECHA
        PasoRecursivo(dibuja, x + largo // 2, y + largo // 2, largo // 2, altura // 2, contador)


def ArbolH():
    ventana = turtle.Screen()
    ventana.setup(700, 700)
    triangulo = turtle.Turtle()
    triangulo.hideturtle()
    triangulo.speed(8)
    PasoRecursivo(triangulo, - 700 / 2, - 700 / 2, 700, 700, 3)
    turtle.done()

def Dado():
    numero = random.randint(1, 6)
    return numero

def Simulaciones(numero):
    resultados = open('resultados.txt','w')
    numero_simulacion = 0
    diccionario1 = {"Numero de simulacion: ": 0, "Resultado obtenido: ": 0}
    lista = [Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1)]
    resultados.write("Numero de simulacion \t Resultado obtenido \t Cocientes n_1 / i \tn_2 / i \t   n_3 / i \t      n_4 / i \t      n_5 / i \t       n_6 / i \n")
    denominador = 1
    for i in range(numero):
        numero_simulacion = i + 1
        j = 1
        while(j <= 8):
            diccionario1["Numero de simulacion: "] = numero_simulacion
            resultados.write(str(diccionario1["Numero de simulacion: "]) + "\t \t \t \t \t")
            diccionario1["Resultado obtenido: "] = Dado()
            resultados.write(str(diccionario1["Resultado obtenido: "] ) + "\t \t \t \t")
            if(diccionario1["Resultado obtenido: "] == 1):
                lista[0] = Fraction(lista[0].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            elif(diccionario1["Resultado obtenido: "] == 2):
                lista[1] = Fraction(lista[1].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            elif(diccionario1["Resultado obtenido: "] == 3):
                lista[2] = Fraction(lista[2].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            elif(diccionario1["Resultado obtenido: "] == 4):
                lista[3] = Fraction(lista[3].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            elif(diccionario1["Resultado obtenido: "] == 5):
                lista[4] = Fraction(lista[4].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            elif(diccionario1["Resultado obtenido: "] == 6):
                lista[5] = Fraction(lista[5].numerator + 1, denominador)
                for i in lista:
                    resultados.write(str(i) + "\t \t \t")
            j += 1
            denominador += 1
            break
        lista = [Fraction(lista[0].numerator,denominador), Fraction(lista[1].numerator,denominador),
        Fraction(lista[2].numerator,denominador), Fraction(lista[3].numerator,denominador),
        Fraction(lista[4].numerator,denominador), Fraction(lista[5].numerator,denominador)]
        resultados.write("\n")
    resultados.close()

def Menu():
    while True:
        print("* 1) Determinar si los elementos de una lista son distintos entre si.")
        print("* 2) Desviacion estandar.")
        print("* 3) Diccionario temperaturas.")
        print("* 4) Mono infiito")
        print("* 5) Fractal.")
        print("* 6) Probabilidad Frecuencial.")
        print("* 7) Salir")
        print("Esocoge un numero: ")
        boton = int(input())
        if(boton == 1):
            print("Digita el numero de elementos de tu lista: ")
            numero = int(input())
            lista = []
            for i in range(numero):
                print("Digita el elemento: ")
                elemento = int(input())
                lista.append(elemento)
            print("Resultado: " + str(DiferenciadorDeNumeros(lista)) + "\n")
        elif(boton == 2):
            print("Digita el numero de elementos de tu lista: ")
            numero = int(input())
            lista2 = []
            for i in range(numero):
                print("Digita el elemento: ")
                elemento = int(input())
                lista2.append(elemento)
            print("Resultado: " + str(DesviacionEstandar(lista2)) + "\n" )
        elif(boton == 3):
            print("Resultado: " + str(DiccionarioTemperaturas()) + "\n")
        elif(boton == 4):
            print("Digita el numero de coincidencias (0,28): ")
            digitos = int(input())
            print(MonoInfinito(digitos))
            print("methinks it is like a weasel")
        elif(boton == 5):
            print("Escoge una opcion:")
            print("1) Triangulo Sierpinski ")
            print("2) Arbol H")
            opcion = int(input())
            if(opcion == 1):
                TrianguloSierpinski()
            if(opcion == 2):
                ArbolH()
        elif(boton == 6):
            print("Digita el número de simulaciones: ")
            digito = int(input())
            print(Simulaciones(digito))
            print("Revisa el archivo con el nombre resultados.")
        elif(boton == 7):
            print("Gracias por usarme :)")
            return
Menu()
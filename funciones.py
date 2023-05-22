#SINTAXIS CLASS
import math
import statistics as stat
from datetime import datetime #Libreria para el tiempo
import random

class Sistema_Inteligente:
    
    #inicializador
    #Valores por defecto: variable = valor en parametros
    def __init__(self, secuencia, menu = 'V'):
        
        self.secuencia = secuencia
        self.menu = menu

    #SINTAXIS FUNCION
    def suma(self, *extra):
        for val in extra:
            self.secuencia.append(val)
        
        resultado = sum(self.secuencia)
        return resultado

    def producto(self):
        resultado = math.prod(self.secuencia)
        return resultado

    def promedio(self):
        resultado1 = sum(self.secuencia) / len(self.secuencia)
        resultado2 = stat.mean(self.secuencia)

        print(resultado1)
        print(resultado2)

    def calculos_electronicos(self):
        if(self.menu == 'V'):
            C = float(input("\nIngrese la corriente: "))
            R = float(input("Ingrese la resistencia: "))
            V = C * R
            
            return V
        elif(self.menu == 'C'):
            V = float(input("\nIngrese el voltaje: "))
            R = float(input("Ingrese la resistencia: "))
            C = V / R
            
            return C
        elif(self.menu == 'R'):
            V = float(input("\nIngrese el voltaje: "))
            C = float(input("Ingrese la corriente: "))
            R = V / C
            
            return R
        else:
            print()

    def calculos_distancias(self):
        if(self.menu == 'D'):
            V = float(input("\nIngrese la velocidad: "))
            T = float(input("Ingrese el tiempo: "))
            D = V * T
            
            return D
        elif(self.menu == 'V'):
            D = float(input("\nIngrese la distancia: "))
            T = float(input("Ingrese el tiempo: "))
            V = D / T
            
            return V
        elif(self.menu == 'T'):
            D = float(input("\nIngrese la distancia: "))
            V = float(input("Ingrese la velocidad: "))
            T = D / V
            
            return T
        else:
            print()
    
    def calculos_temperaturas(self):
        if(self.menu == "CF"):
            C = float(input("\nTemperatura Celsius: "))
            F = (C * 1.8)+32

            return F
        elif(self.menu == "CK"):
            C = float(input("\nTemperatura Celsius: "))
            K = C+273.15

            return K
        elif(self.menu == "FC"):
            F = float(input("\nTemperatura Farenheit: "))
            C = (F-32)/1.8

            return C
        elif(self.menu == "FK"):
            F = float(input("\nTemperatura Farenheit: "))
            K = ((F-32)/1.8)+273.15
            
            return K
        elif(self.menu == "KC"):
            K = float(input("\nTemperatura Kelvin: "))
            C = K-273.15

            return C
        elif(self.menu == "KF"):
            K = float(input("\nTemperatura Kelvin: "))
            F = ((K-273.15) * 1.8)+32

            return F
        else:
            print()

    def calculos_cubo(self):
        if(self.menu == "A"):
            Longitud = float(input("\nIngrese la Longitud: "))
            Ancho = float(input("Ingrese el Ancho: "))
            Area = Longitud * Ancho

            return Area
        elif(self.menu == "P"):
            Longitud = float(input("\nIngrese la Longitud: "))
            Ancho = float(input("Ingrese el Ancho: "))
            Perimetro = Longitud + Ancho + Longitud + Ancho

            return Perimetro
        elif(self.menu == "V"):
            Longitud = float(input("\nIngrese la Longitud: "))
            Ancho = float(input("Ingrese el Ancho: "))
            Altura = float(input("Ingrese la Altura: "))
            Volumen = Longitud * Ancho * Altura

            return Volumen
        elif(self.menu == "S"):
            Longitud = float(input("\nIngrese la Longitud: "))
            Ancho = float(input("Ingrese el Ancho: "))
            Altura = float(input("Ingrese la Altura: "))
            Superficie = (Longitud * Ancho * 2) + (Longitud * Altura * 2) + (Ancho * Altura * 2)
            
            return Superficie
        else:
            print()

    def crear_batido(self):
        fruits = ["Apple", "Banana", "Cherry", "Berries", "Watermelon", "Kiwi", "Coco", "Peach"]
        complements = ["Granola", "Cereal"]
        liquids = ["Agua", "Leche"]

        random.shuffle(fruits)
        random.shuffle(complements)
        random.shuffle(liquids)

        Fruta_1 = fruits[random.randint(0, (len(fruits)-1))]
        Fruta_2 = fruits[random.randint(0, (len(fruits)-1))]
        compl = complements[random.randint(0, (len(complements)-1))]
        liqui = liquids[random.randint(0, (len(liquids)-1))]

        print("\nFELICIDADES. Te has ganado un batido gratis de {:s}, {:s}, {:s} y {:s}".format(Fruta_1, Fruta_2, compl, liqui))

    def conversiones_trig(self):
        if(self.menu == "GR"):
            inp_grados = float(input("\nIngrese el numero de grados: "))
            radianes = math.radians(inp_grados)

            print("\n{:,.2f} Grados es igual a {:,.2f} Radianes".format(inp_grados, radianes))
        elif(self.menu == "RG"):
            inp_radianes = float(input("\nIngrese el numero de radianes: "))
            grados = math.degrees(inp_radianes)

            print("\n{:,.2f} Radianes es igual a {:,.2f} Grados".format(inp_radianes, grados))
        elif(self.menu == "SCT"):
            numb = float(input("\nIngrese su numero: "))

            sin = math.sin(numb)
            cos = math.cos(numb)
            tan = math.tan(numb)

            print("\nSeno: {:,.2f}".format(sin))
            print("Coseno: {:,.2f}".format(cos))
            print("Tangente: {:,.2f}".format(tan))

    def nota_SI(self):
        nombre = input("\nIngrese su nombre: ")

        rand = random.random()*100
        print("\nEl alumno {:s} tiene una probabilidad de {:,.2f}{:s} de pasar la clase de Sistemas Inteligentes".format(nombre, rand, '%'))

    def date_time_update(self):
        actual_time = datetime.now()

        str_dt = actual_time.strftime("%d/%m/%Y | %H:%M:%S")

        return str_dt
    

print("BIENVENIDO AL PRGRAMA")
opcion = -1
while(opcion != 0):
    print("\nSeleccione el codigo que desea ejecutar")
    print("1) Calculos con secuencia")
    print("2) Calculos electricos")
    print("3) Calculos distancias")
    print("4) Calculos temperaturas")
    print("5) Calculo de dimensiones")
    print("6) Batidos aleatorios")
    print("7) Cauclos trigonometricos")
    print("8) Notas de SI")
    print("0) SALIR")
    opcion = int(input("Opcion: "))

    if(opcion == 0):
        break

    elif(opcion == 1):
        print()
        time_object = Sistema_Inteligente([], 0)
        print(time_object.date_time_update())
        
        num_datos = int(input("Ingrese numero de datos: "))
        secuencia = []

        for dato in range(num_datos):
            valor = int(input("Ingrese el dato: "))
            secuencia.append(valor)

        obj_1 = Sistema_Inteligente(secuencia, "")
        datos = obj_1.secuencia
        print("Arreglo (sin extra): {}".format(datos))
        print(obj_1.suma(10, 20, 30))
        print(obj_1.producto())
        obj_1.promedio()

    elif(opcion == 2):
        opcion2 = -1
        while(opcion2 != 0):
            print()
            time_object = Sistema_Inteligente([], 0)
            print(time_object.date_time_update())
            print("\nSeleccione el valor que desea calcular")
            print("1) Voltaje")
            print("2) Corriente")
            print("3) Resistencia")
            print("0) SALIR")
            opcion2 = int(input("Seleccion: "))
            if(opcion2 == 0):
                break
            elif(opcion2 == 1):
                electronic = "V"
                obj_2 = Sistema_Inteligente([])
                print("\nVoltaje: {} V".format(obj_2.calculos_electronicos()))
            elif(opcion2 == 2):
                electronic = "C"
                obj_2 = Sistema_Inteligente([], electronic)
                print("\nCorriente: {} i".format(obj_2.calculos_electronicos()))
            elif(opcion2 == 3):
                electronic = "R"
                obj_2 = Sistema_Inteligente([], electronic)
                print("\nResistencia: {} R".format(obj_2.calculos_electronicos()))

    elif(opcion == 3):
        opcion2 = -1
        while(opcion2 != 0):
            print()
            time_object = Sistema_Inteligente([], 0)
            print(time_object.date_time_update())
            print("\nSeleccione el valor que desea calcular")
            print("1) Distancia")
            print("2) Velocidad")
            print("3) Tiempo")
            print("0) SALIR")
            opcion2 = int(input("Seleccion: "))
            if(opcion2 == 0):
                break
            elif(opcion2 == 1):
                distances = "D"
                obj_2 = Sistema_Inteligente([], distances)
                print("\nDistancia: {} metros".format(obj_2.calculos_distancias()))
            elif(opcion2 == 2):
                distances = "V"
                obj_2 = Sistema_Inteligente([], distances)
                print("\nVelocidad: {} m/h".format(obj_2.calculos_distancias()))
            elif(opcion2 == 3):
                distances = "T"
                obj_2 = Sistema_Inteligente([], distances)
                print("\nTiempo: {} horas".format(obj_2.calculos_distancias()))

    elif(opcion == 4):
        opcion2 = -1
        while(opcion2 != 0):
            print()
            time_object = Sistema_Inteligente([], 0)
            print(time_object.date_time_update())
            print("\nSeleccione la temperatura desea calcular")
            print("1) Celsius a Farenheit")
            print("2) Celsius a Kelvin")
            print("3) Farenheit a Celsius")
            print("4) Farenheit a Kelvin")
            print("5) Kelvin a Celsius")
            print("6) Kelvin a Farenheit")
            print("0) SALIR")
            opcion2 = int(input("Seleccion: "))
            if(opcion2 == 0):
                break
            elif(opcion2 == 1):
                temp = "CF"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Farenheit: {}° grados".format(obj_2.calculos_temperaturas()))
            elif(opcion2 == 2):
                temp = "CK"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Kelvin: {}° grados".format(obj_2.calculos_temperaturas()))
            elif(opcion2 == 3):
                temp = "FC"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Celsius: {}° grados".format(obj_2.calculos_temperaturas()))
            elif(opcion2 == 4):
                temp = "FK"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Kelvin: {}° grados".format(obj_2.calculos_temperaturas()))
            elif(opcion2 == 5):
                temp = "KC"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Celsius: {}° grados".format(obj_2.calculos_temperaturas()))
            elif(opcion2 == 6):
                temp = "KF"
                obj_2 = Sistema_Inteligente([], temp)
                print("\nTemperatura Farenheit: {}° grados".format(obj_2.calculos_temperaturas()))

    elif(opcion == 5):
        opcion2 = -1
        while(opcion2 != 0):
            print()
            time_object = Sistema_Inteligente([], 0)
            print(time_object.date_time_update())
            print("\t\nCALCULO DE DIMENSIONES")
            print("\n1) Area")
            print("2) Perimetro")
            print("3) Volumen")
            print("4) Superficie")
            print("0) SALIR")
            opcion2 = int(input("Selccion: "))
            if(opcion2 == 0):
                break
            elif(opcion2 == 1):
                dims = "A"
                obj_2 = Sistema_Inteligente([], dims)
                print("El Area descrita es de {:,.2f} metros".format(obj_2.calculos_cubo()))
            elif(opcion2 == 2):
                dims = "P"
                obj_2 = Sistema_Inteligente([], dims)
                print("El Perimetro descrito es de {:,.2f} metros".format(obj_2.calculos_cubo()))
            elif(opcion2 == 3):
                dims = "V"
                obj_2 = Sistema_Inteligente([], dims)
                print("El Volumen descrito es de {:,.2f} metros".format(obj_2.calculos_cubo()))
            elif(opcion2 == 4):
                dims = "S"
                obj_2 = Sistema_Inteligente([], dims)
                print("La Superficie descrita es de {:,.2f} metros".format(obj_2.calculos_cubo()))

    elif(opcion == 6):
        print()
        time_object = Sistema_Inteligente([], 0)
        print(time_object.date_time_update())

        bat = "B"
        obj_2 = Sistema_Inteligente([], bat)
        obj_2.crear_batido()

    elif(opcion == 7):
        opcion2 = -1
        while(opcion2 != 0):
            print()
            time_object = Sistema_Inteligente([], 0)
            print(time_object.date_time_update())
            print("\t\nCALCULOS TRIGONOMETRICOS")
            print("\n1) Grados a Radianes")
            print("2) Radianes a Grados")
            print("3) Seno, Coseno y Tangente")
            print("0) SALIR")
            opcion2 = int(input("Selccion: "))
            if(opcion2 == 0):
                break
            elif(opcion2 == 1):
                trig = "GR"
                obj_2 = Sistema_Inteligente([], trig)
                obj_2.conversiones_trig()
            elif(opcion2 == 2):
                trig = "RG"
                obj_2 = Sistema_Inteligente([], trig)
                obj_2.conversiones_trig()
            elif(opcion2 == 3):
                trig = "SCT"
                obj_2 = Sistema_Inteligente([], trig)
                obj_2.conversiones_trig()   

    elif(opcion == 8):
        note = "N"
        obj_2 = Sistema_Inteligente([], note)
        obj_2.nota_SI()

    else:
        print("\nLa opcion elegida es incorrecta")


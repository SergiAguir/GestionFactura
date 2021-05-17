from factura import Factura
from controlador import Controlador
from datetime import datetime

con = Controlador()

while True:
    print("El numero total de facturas disponibles es ",con.getNumFacturas())
    print("1.- Anyadir Factura")
    print("2.- Listar Facturas pendientes de pago")
    print("3.- Listar Facturas pagadas")
    print("4.- Pagar factura")
    print("5.- Salir")

    op = int(input("Selecciona una opcion: "))

    if op == 1:
        while True:
            try:
                id = int(input("Introduce un Id: "))
                break
            except ValueError:
                print("-------------------------------")
                print("Error en la introduccion del Id")
                print("-------------------------------")

        while True:
            fecha = datetime.now()
            fechaForm = fecha.strftime("%d/%m/%Y %H:%M")
            print("--------------")
            print("Fecha anyadida")
            print("--------------")
            break

        while True:
            nifE = str(input("Introduce el NIF Emisor: "))

            if nifE == "":
                print("--------------------------------------")
                print("El NIF Emisor no puede estar en blanco")
                print("--------------------------------------")
            else:
                break
        
        while True:
            nifR = str(input("Introduce el NIF Receptor: "))

            if nifR == "":
                print("----------------------------------------")
                print("El NIF Receptor no puede estar en blanco")
                print("----------------------------------------")
            else:
                break
        

        fact = Factura(id,fecha,nifE,nifR)

        if con.anyadirFactura(fact) == False:
            print("Error al anyadir la factura!!!!")
        else:
            print("Factura anyadida correctamente")

        
            print(con.getProductos())
            print("4.- No anyadir mas productos")

            while True:
            
                prod = input("Selecciona una opcion (Pulsa 4 para salir): ")

                

                if prod == "4":
                    print("Saliendo...")
                    break
                else:
                    cant = int(input("Que cantidad quieres anyadir?: "))
                    if con.anyadirLineaFactura(id,prod,cant) == True:
                        print("La linea de factura a sido anyadida corectamente!!")
                    else:
                        print("Error al crear la factura")

        print("Factura creada!!!")

    if op == 2:
        print("Como quieres listar las facturas PENDIENTES de pago?")
        print("1.- Todas las facturas")
        print("2.- Las introducidas por DNI EMISOR")
        print("3.- Las introducidas por DNI RECEPTOR")

        while True:
            try:
                op2 = int(input("Selecciona una opcion: "))
                if op<1 or op>3:
                    print("El numero introducido tiene que ser entre 1 y 3!!")
                else:
                    break
            except ValueError:
                print("El caracter introducido tiene que ser un nuemro!!")

        if op2 == 1:
            for i in con.mostrarFacturas(False,1):
                print(i)

        if op2==2:
            dni=input("Introduce el dni del Emisor: ")
            for i in con.mostrarFacturas(False,2,dni):
                print(i)
            
        if op2==3:
            dni=input("Introduce el dni del Receptor: ")
            for i in con.mostrarFacturas(False,3,dni):
                print(i)

    if op == 3:
        print("Como quieres listar las facturas PAGADAS?")
        print("1.- Todas las facturas")
        print("2.- Las introducidas por DNI EMISOR")
        print("3.- Las introducidas por DNI RECEPTOR")

        while True:
            try:
                op2 = int(input("Selecciona una opcion: "))
                if op<1 or op>3:
                    print("El numero introducido tiene que ser entre 1 y 3!!")
                else:
                    break
            except ValueError:
                print("El caracter introducido tiene que ser un nuemro!!")

        if op2 == 1:
            for i in con.mostrarFacturas(True,1):
                print(i)

        if op2==2:
            dni=input("Introduce el dni del Emisor: ")
            for i in con.mostrarFacturas(True,2,dni):
                print(i)
            
        if op2==3:
            dni=input("Introduce el dni del Receptor: ")
            for i in con.mostrarFacturas(True,3,dni):
                print(i)


    if op == 4:
        id_fact=int(input("Introduce el id de la factura: "))

        if con.facturaPagada(id_fact):
            print("Factura Pagada!")
        else:
            print("Error al pagar la factura!")

    if op == 5:
        print("Adios!!")
        break

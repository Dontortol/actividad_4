# Ejercicio 1
'''
departamentos = ['Alta Verapaz','Baja Verapaz', 'Chimaltenango','Chiquimula','Guatemala',
                 'El Progreso','Escuintla','Huehuetenango','Izabal','Jalapa','Jutiapa','Peten',
                 'Quetzaltenango','Quiche','Retalhuleu','Sacatepequez','San Marcos','Santa Rosa',
                 'Solola','Suchitepequez','Totonicapan','Zacapa']




while True:
    print("----Bienvenido al programa de votacion----")
    name = input("> Introduce tu nombre: ")
    if len(name) < 5:
        print("nombre invalido")
    else:
        print("Nombre registrado")

    while True:
        dpi = (input("> Introduce tu dpi: "))
        if len(dpi) != 13:
            print("su DPI no es valido")
        else:
            print("su DPI es valido")
            break
    while True:
        print(f"{'   1)Alta Verapaz':<20}{'   2)Baja Verapaz':<20}{'   3)Chimaltenango':<20}{'   4)Chiquimula'}")
        print(f"{'   5)Guatemala':<20}{'   6)El Progreso':<20}{'   7)Escuintla':<20}{'   8)Huehuetenango'}")
        print(f"{'   9)Izabal':<20}{'   10)Jalapa':<20}{'   11)Jutiapa':<20}{'   12)Peten'}")
        print(f"{'   13)Quetzaltenango':<20}{'   14)Quiche':<20}{'   15)Retalhuleu':<20}{'   16)Sacatepequez'}")
        print(f"{'   17)San Marcos':<20}{'   18)Santa Rosa':<20}{'   19)Solola':<20}{'   20)Suchitepequez'}")
        print(f"{'   21)Totonicapan':<20}{'   22)Zacapa'}")
        depart = int(input("> Ingrese el departamento donde recide: "))
        if 1 <= depart <= 22:
            departamento = departamentos[depart - 1]
            break
        else:
            print("Lo siento, no esta dentro del rango, vuelva a intentar")

    while True:
        date = int(input("> Ingrese su año de nacimiento: "))
        if date <= 2007:
            print("Edad aceptada")
        print(f"Bienvenido {name}, su centro de votacion es en {departamentos[depart - 1]} ")
        break
    break
'''

# Ejercico 2

while True:
    print("----Bienvenido al programa de impuestos progresivos----")
    annual = int(input("> Introduce tus ingresos anuales: "))
    dependent = int(input("> Introduce el numero de dependientes: "))
    dependent2 = 1000 * dependent
    if annual >= 0 and annual <= 30000:
        print("Impuesto a pagar:")
        print("Q.",annual * 0.05, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.05 + dependent2)
        break
    if annual >= 30001 and annual <= 60000:
        print("Impuesto a pagar:")
        print("Q.", annual * 0.1, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.1 + dependent2)
        break
    if annual >= 60001 and annual <= 100000:
        print("Impuesto a pagar:")
        print("Q.", annual * 0.15, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.15 + dependent2)


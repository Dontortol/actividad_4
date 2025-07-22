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
from platform import processor

# Ejercico 2
'''
while True:
    print("----Bienvenido al programa de impuestos progresivos----")
    annual = int(input("> Introduce tus ingresos anuales: "))
    dependent = int(input("> Introduce el numero de dependientes: "))
    dependent2 = 1000 * dependent
    if annual >= 0 and annual <= 40000 and dependent >= 2:
        print("No debe pagar impuestos")
        break
    elif annual >= 0 and annual <= 30000:
        print("Impuesto a pagar:")
        print("Q.",annual * 0.05, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.05 + dependent2)
        break
    elif annual >= 30001 and annual <= 60000:
        print("Impuesto a pagar:")
        print("Q.", annual * 0.1, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.1 + dependent2)
        break
    elif annual >= 60001 and annual <= 100000:
        print("Impuesto a pagar:")
        print("Q.", annual * 0.15, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.15 + dependent2)
        break
    elif annual >= 100001:
        print("Impuesto a pagar:")
        print("Q.", annual * 0.2, ", por el numero de dependientes su pago final sera de", "Q.", annual * 0.2 + dependent2)
    else:
        print("ingrese bien los datos solicitados")
'''
# Ejercicio 3
'''
class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password

users =[
    Users("Rodrigo", "12345" ),
    Users("Rene", "6789"),
    Users("Ricky", "hola"),
]
tries = 0

while tries < 3:
    print("----Ingresa tu nombre de usuario y contraseña (Escribe 1 en el usuario para salir)----")
    for a in users:
        user = input("> Introduce tu nombre: ")
        if user == "1":
            print("Saliendo del sistema")
            break
        password1 = input("> Introduce tu contraseña: ")
        if a.name != users and a.password != password1:
            print("Usuario o contraseña incorrecta, vuelve a intentar ")
            tries += 1
        if tries == 3:
            print("Cuenta bloqueada")
        for i in users:
            if i.name == user and i.password == password1:
                print(f"Bienvenido al menu {i.name}")
                while True:
                    print("1. Ver perfil\n"
                          "2. Cambiar contraseña\n"
                          "3. Cerrra sesion")
                    select = input("Ingrese la opcion que quiera: ")
                    if select == "1":
                        print(f"Nombre de usuario: {i.name}\n"
                              f"Tu contraseña es: {i.password}\n"
                              f"")
                        continue
                    elif select == "2":
                        password2 = input("Ingrese su contraseña: ")
                        for u in users:
                            if u.password == password2:
                                change_pass = input("Ingrese nueva contraseña: ")
                                u.password = change_pass
                                print(f"Tu nueva contraseña es: {change_pass}")
                                break
                    elif select == "3":
                        print("Cerrando sesion")
                        break
                    break
                break
'''
# Ejercicio 4

prices = []
while True:
    print("productos de mercado")
    print("1. Agegar producto \n"
          "2. Continuar\n"
          "3. Ver carrito")
    select = input("Ingrese la opcion que quiera: ")
    if select == "1":
        price = int(input("> Ingrese precio del producto: "))
        prices.append(price)
    elif select == "3":
        print(prices)
    elif select == "2":
        while True:
            tips = input("Desea dejar propina?: ")
            if tips == "si":
                tip = float(input("> Ingrese la propina que quiere dejar en porcentaje: "))
                tip = tip
            elif tips == "no":
                continue
                discount_card = input("> Tiene tarjeta de descuento?: ")
                if discount_card == "si":
                    discount = prices * 0.1
                    print("Se ha descontado un 10%")
                elif discount_card == "no":
                    continue



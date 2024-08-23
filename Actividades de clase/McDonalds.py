Inventario = [{"Nombre":"McFlury", "Precio":2.5, "Cantidad": 10}]

def Menu_principal ():
    while True:
        print("")
        print("-" * 18, "Menu Principal", "-" * 18)
        print("1. agregar producto")
        print("2. mostrar inventario")
        print("3. Vender produto")
        print("4. Salir")
        print("")
        opcion = input("Seleccione una opcion: ")
        print("-" * 52)
        print("") 
        
        if opcion == "1":
            agregar_produto()
        elif opcion == "2":
            Monstrar_inventario()
        elif opcion == "3":
            Venta()
        elif opcion == "4":
            print("Saliendo.....")
            print("")
            break
        else:
            print("Opcion no valida")

def agregar_produto ():
    
    while True:
        Nombre = input("Ingrese el nombre del produto: ")
        if Nombre != "" and Nombre != " ":
            break
    
    precio = float(input("Ingrese el precio del produto: "))
    cantidad = int(input("Ingrese la cantidad del produto: "))
    
    producto = {"Nombre": Nombre, "Precio": precio, "Cantidad": cantidad}
    Inventario.append(producto)
    
    print("")
    print(f"Producto {Nombre} agrgado con exito 👍")
    print(Inventario)

def Monstrar_inventario():
    if len(Inventario) == 0:
        print("El inventario esta vacio")
    else:
        print("*" * 17, "Inventario", "*" * 17)
        for producto in Inventario:
            print(f"Nombre: {producto['Nombre']} - Precio: {producto['Precio']:.2f} - Cantidad: {producto['Cantidad']}")
            print("*" * 46)

def Venta():
    nombre = input("Ingrese el producto que desea vender: ")
    
    for producto in Inventario:
        if producto["Nombre"].lower() == nombre.lower():
            cantidad = int(input("Cuantas unidades vendera: "))
            if cantidad <= producto["Cantidad"]:
                producto["Cantidad"] -= cantidad
                total = cantidad * producto["Precio"]
                print("")
                print(f"Venta realizada. Total: ${total:.2f}")
                
                if producto["Cantidad"] != 0:
                    print(f"Quedan {producto['Cantidad']} unidades de {nombre}")
                else:
                    print(f"{nombre} agotado")
                    Inventario.remove(producto)
                return
            else:
                print("No hay suficientes unidades")
                return
        else:
            print("Producto no existente")
            return

Menu_principal()
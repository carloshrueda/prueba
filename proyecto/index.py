from modulo.nuevo_facturar import facturacion
from interfaz.menu import menuu
while True:
    opc = menuu()
    match opc:
        case "1":
            facturacion()
        case "2":
            pass
        case "3":
            pass
        case "4":
            print("gracias por usar el programa")
            break


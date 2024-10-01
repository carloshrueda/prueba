
def menuu():
    while True:
        print("** MENU**")
        print("1. imprimir una copia de una factura.")
        print("2. Imprimir un resumen por cliente.")
        print("3. Un diagrama de barras que muestre gráficamente un comparativo de los valores de las facturas de los meses de un año.")
        print("4.salir")

        print(">> Ingresar a opcion: ", end="")
        try:
            opciones = ["1", "2", "3","4"]
            opc = input()
            if opc not in opciones:
                print("Error opcion invalida")
                print("presione cualquier tecla para volver al menu. \n")
            return opc
        
        except ValueError:
            print("ingreso una opcion incorrecta")
            print("presione cualquier tecla para volver al menu. \n")
         

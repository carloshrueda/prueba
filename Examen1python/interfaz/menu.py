def menu():
    while True:
        print('MENÚ')
        print('1. Copia de la factura')
        print('2. Resumen de la factura en un mes especifico')
        print('3. Diagrama comparativo')
        print('4. Productos comunes entre clientes')
        print('5. Salir')
        print('>>> Opcion? ', end='')
        try:
            opcion = int(input())
            if opcion < 1 or opcion > 5:
                print('Error. Opción no válida.')
                print('Presione cualquier tecla para volver al menú...')
                continue
            return opcion
        except ValueError:
            print('Error. Opción no válida.')
            print('Presione cualquier tecla para volver al menú...')
    
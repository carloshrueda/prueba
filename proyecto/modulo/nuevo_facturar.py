
def cliente_code():
    client = input("ingrese el codigo del cliente: \n")
    letter = open("/home/camper/Documentos/proyecto/productos/clientes.dat")
    for line in letter:
        if line.startswith(client):
            new = line.split(';')
            code = new [0]
            return code
        
def nombre_cliente():
    name = cliente_code()
    letter = open("/home/camper/Documentos/proyecto/productos/clientes.dat")
    #new = letter.read()
    #print(new)
    for line in letter:
        if line.startswith(name):
            new = line.split(';')
            nombre = new [1]
            return nombre
        
def telefono_cliente():
    number = cliente_code()
    letter = open("/home/camper/Documentos/proyecto/productos/clientes.dat")
    #new = letter.read()
    #print(new)
    for line in letter:
        if line.startswith(number):
            new = line.split(';')
            nombre = new [1]
            return nombre
def producto():
        number = cliente_code()
        ventas = open("/home/camper/Documentos/proyecto/productos/ventas.dat")
        productos = open("/home/camper/Documentos/proyecto/productos/productos.dat")
        if cliente_code in ventas:
        pass


def facturacion():
        print("Resumen de todas las facturas de un cliente de un mes solicitado.")
        cod = cliente_code()
        nombre = nombre_cliente()
        telefono = telefono_cliente()

        print("====================")
        print("  FACTURACIÓN DEL 2024")
        print("====================")
        print("codigo", cod)
        print("Nombre", nombre)
        print("Telefono", telefono)
        print("___Productos________")
        print("producto code : ",   "Nombre del producto: ")

        
    
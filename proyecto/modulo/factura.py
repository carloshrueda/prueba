#lo que se quiere es bucar clientes mediante su 
print("Resumen de todas las facturas de un cliente de un mes solicitado.")
client = input("ingrese el codigo del cliente: \n")

letter = open("/home/camper/Documentos/proyecto/productos/clientes.dat")
#new = letter.read()
#print(new)
for line in letter:
    if line.startswith(client):
        new = line.split(';')
        codigo = new [0]
        nombre = new [1]
        telefono = new[2]


 
def factura():
      print("====================")
      print("  FACTURACIÓN DEL 2024")
      print("====================")
      print("Codigo:", codigo)
      print("Nombre", nombre)
      print("telefono", telefono)


        

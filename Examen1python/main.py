def read_file (filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        return[lines.strip().split(',')for line in lines]
productos=read_file('productos.dat')
clientes=read_file('clientes.dat')
ventas=read_file('ventas.dat')

def imprimirfac(n):
    for f in range(len(n)):
        for c in range(len(n[f])):
            print(n[f][c], end= "\t")

fd = open ('clientes.dat','r')
clientes=[]

for linea in fd:
    clientes.append(linea.split(','))
imprimirfac(clientes)

fd =productos ('productos.dat''r')
productos=[]

for linea in fd:
    productos.append(linea.split(','))
imprimirfac(productos)

fd= open ('ventas.dat')
ventas=[]
for linea in fd:
    ventas.append(linea.split(','))
imprimirfac(ventas)

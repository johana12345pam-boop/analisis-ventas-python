import csv

total_ventas = 0
total_productos = 0

with open('ventas.csv', newline='') as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        precio = float(fila['precio'])
        cantidad = int(fila['cantidad'])
        
        total_ventas += precio * cantidad
        total_productos += cantidad

print("Total de ventas:", total_ventas)
print("Total de productos vendidos:", total_productos)
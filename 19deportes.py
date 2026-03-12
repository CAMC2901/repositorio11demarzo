acum1=0
acum2=0
acum3=0
for i in range (10):
    nombre=str(input("ingrese el nombre del producto:"))
    disp=int(input("ingrese la cantidad disponible: "))
    if disp ==0:
        print("el producto no esta disponible")
        acum1+=1
    elif disp > 0 and disp <= 5:
        acum2+=1
        print("stock bajo")
    elif disp >= 6:
        acum3+=1
        print("stock normal")
print("el numero de productos no disponibles es: ", acum1)
print("el numero de productos con stock bajo es: ", acum2)
print("el numero de productos con stock normal es: ", acum3)
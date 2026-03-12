acum_alimento=0
acum_juguete=0
acum_accesorio=0
acum1=0
acum2=0
acum3=0
for i in range(10):
    categoria=int(input("ingrese la categoria\n  1.alimento\n  2.juguete\n  3.accesorio\n"))
    if categoria == 1:
        acum1+=1
        compra=int(input("ingrese el valor de la compra: "))
        acum_alimento+=compra
    elif categoria == 2:
        acum2+=1
        compra=int(input("ingrese el valor de la compra: "))
        acum_juguete+=compra
    else:
        acum3+=1
        compra=int(input("ingrese el valor de la compra: "))
        acum_accesorio+=compra
print("el total de dinero gastado en alimento es: ", acum_alimento)
print("el total de dinero gastado en juguete es: ", acum_juguete)
print("el total de dinero gastado en accesorio es: ", acum_accesorio)
if acum1 > acum2 and acum1 > acum3:
    print("la categoria mas comprada es alimento")
elif acum2 > acum1 and acum2 > acum3:
    print("la categoria mas comprada es juguete")
else:
    print("la categoria mas comprada es accesorio")
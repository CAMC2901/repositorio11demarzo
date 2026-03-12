acum_corte=0
acum_cepillado=0
acum_tintura=0
acum=0
for i in range(7):
    nombre=input("ingrese el nombre del cliente: ")
    servicio=int(input("ingrese el servicio\n 1. corte\n 2. cepillado\n 3. tintura\n"))

    if servicio == 1:
        precio=int(input("ingrese el valor de la compra: "))
        acum_corte+=1
        acum+=precio
        
    elif servicio == 2:
        precio=int(input("ingrese el valor de la compra: "))
        acum_cepillado+=1
        acum+=precio
    else:
        precio=int(input("ingrese el valor de la compra: "))
        acum_tintura+=1
        acum+=precio
print("el total del dia es: ", acum)
print("el numero de cortes es: ", acum_corte)
print("el numero de cepillados es: ", acum_cepillado)
print("el numero de tinturas es: ", acum_tintura)
if acum_corte > acum_cepillado and acum_corte > acum_tintura:
    print("el servicio mas solicitado es corte")
elif acum_cepillado > acum_corte and acum_cepillado > acum_tintura:
    print("el servicio mas solicitado es cepillado")
else:
    print("el servicio mas solicitado es tintura")
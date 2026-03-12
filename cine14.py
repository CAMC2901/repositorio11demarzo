acum_niños=0
acum_adulto=0
acum_adultomayor=0
acum_per=0
boletos=""
personas=0
capacidad=int(input("cual es la capacidad de la sala:"))
while acum_per<=capacidad and boletos!="salir":
    boletos=str(input("comprar, salir: "))
    if boletos=="comprar":
        personas=int(input("cuantas personas van a ingresar a la sala: "))
        if acum_per+personas>capacidad:
           print("no hay suficientes cupos")
        else:
           acum_per+=personas
        for i in range(personas):
            edad=int(input(" ponga su edad: "))
            if edad<18:
                acum_niños+=1
                print("niño")
            elif edad>=18 and edad<60:
                acum_adulto+=1
                print("adulto")
            elif edad>=60:
                acum_adultomayor+=1
                print("adulto mayor")
            elif boletos=="salir":
             print("saliendo")
print(f"ingresaron {acum_per} personas.")
print(f"ingresaron {acum_niños} niños, {acum_adulto} adultos, {acum_adultomayor} adultos mayores.")
if acum_per == capacidad:
   print("se lleno la sala")
else:
   print("no se lleno la sala")
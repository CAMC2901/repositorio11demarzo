cono=3000
vaso=4000
banana_split=9000
cliente=""
acum3=0
acum2=0
acum1=0
acum_total=0
while cliente != 4:
    cliente=int(input("1. cono, 2.vaso, 3. banana split, 4. salir"))
    if cliente == 1:
        cant=int(input("cuantos conos quiere: "))
        total=cant*cono
        acum1+=1
        acum_total+=total
        print(total)
    elif cliente == 2:
         cant=int(input("cuantos vasos quiere: "))
         total=cant*vaso
         acum2+=1
         acum_total+=total
         print(total)
    elif cliente == 3:
        cant=int(input("cuantos banana split quiere: "))
        total=cant*banana_split
        acum3+=1
        acum_total+=total
        print(total)
    elif cliente == 4:
        print("saliendo")
        if acum1>acum2 and acum1>acum3:
            print(f"cono se pidio {acum1} veces")
        elif acum2>acum1 and acum2>acum3:
            print(f"vaso se pidio {acum2} veces")
        else: 
            acum3>acum1 and acum3>acum1
            print(f"banana split se pidio {acum3} veces")
total_clientes=acum1+acum2+acum3
print("total vendido", acum_total)
print(f"se atendieron {total_clientes} clientes")

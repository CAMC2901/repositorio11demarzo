cafe=4000
capuchino=7000
pastel=6000
compra=""
acum=0
while compra != "salir":
    compra=str(input("cafe, capuchino, pastel, salir"))
    if compra == "cafe":
        acum+=cafe
    elif compra=="capuchino":
        acum+=capuchino
    elif compra == "pastel":
        acum+=pastel
    elif compra == "salir":
        print("saliendo")
if acum>20000:
    total=acum*0.90
    print(total)
else:
    print(acum)
     
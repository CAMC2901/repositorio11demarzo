cafe=4000
te=3500
jugo=5000
pedido=int(input("1. cafe, 2. te, 3. jugo"))
if pedido == 1:
    cant=int(input("cuantos cafe quiere: "))
    total=cant*cafe
    print("total de su compra es: ", total)
elif pedido == 2:
    cant=int(input("cuantos te quiere: "))
    total=cant*te
    print("el total de su compra es: ", total)
else:
    cant=int(input("cuantos jugos quiere: "))
    total=cant*jugo
    print("el total de su compra es: ", total)
    

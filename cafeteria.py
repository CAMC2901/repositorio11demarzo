cafe=4000
te=3500
jugo=5000
pedido=int(input("1. cafe, 2. te, 3. jugo"))
if pedido == 1:
    cant_cafe=int(input("cuantos cafe quiere: "))
    total_cafe=cant_cafe*cafe
    print("total de su compra es: ", total_cafe)
elif pedido == 2:
    cant_te=int(input("cuantos te quiere: "))
    total_te=cant_te*te
    print("el total de su compra es: ", total_te)
else:
    cant_jugo=int(input("cuantos jugos quiere: "))
    total_jugo=cant_jugo*jugo
    print("el total de su compra es: ", total_jugo)
    
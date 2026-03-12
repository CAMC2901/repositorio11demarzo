basico=50000
premiun=90000
familiar=130000
acum=0
cont_basico=0
cont_premium=0
cont_familiar=0
n=int(input("ingrese el numero de clientes: "))
for i in range(n):
    nombre=input("ingrese el nombre del cliente: ")
    edad=int(input("ingrese la edad del cliente: "))
    if edad < 18:
        print("registro juvenil")
    elif edad>=60:
        print("beneficio senior")
    plan=int(input("ingrese el plan\n 1. plan basico\n 2. plan premium\n 3. olan familiar\n"))
    if plan == 1:
        cont_basico+=1
        acum+=basico
        print("el valor a pagar es: ", basico)
    elif plan == 2:
        cont_premium+=1
        acum+=premiun
        print("el valor a pagar es: ", premiun)
    else:
        cont_familiar+=1
        acum+=familiar
        print("el valor a pagar es: ", familiar)
print("el total recaudado es: ", acum)
print("el numero de clientes con plan basico es: ", cont_basico)
print("el numero de clientes con plan premium es: ", cont_premium)
print("el numero de clientes con plan familiar es: ", cont_familiar)
if cont_basico > cont_premium and cont_basico > cont_familiar:
    print("el plan mas vendido es el basico")
elif cont_premium > cont_basico and cont_premium > cont_familiar:
    print("el plan mas vendido es el premium")
else:
    print("el plan mas vendido es el familiar")
carro=4000
moto=2000
acum_carro=0
acum_moto=0
placa=[]

for i in range(8):
    placa=input("ingrese su placa: ")
    tipo=int(input("1. carro, 2. moto: "))
    horas=int(input("horas de parqueo: "))
    if tipo == 1:
        acum_carro+=1
        total=horas*carro
        print(total)
    else:
        acum_moto+=1
        total=horas*moto
        print(total)
print(max(placa))
